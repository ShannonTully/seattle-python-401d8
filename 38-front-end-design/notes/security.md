# Django Auth-Auth & Security

## What is Authentication?

**Authentication** checks whether or not a user is who they say that they are
(or if they are anyone at all). We can use authentication (AuthN) rules to
restrict site access to “members only”, or to serve different views to
different types of users. Let’s see how this works in Django

## Authentication in Django

In Django, authentication is granted upon valid user login. Currently, our
user authentication is handled by the `django-registration` package. However,
this just declares the logged-in user as authenticated. How do we control
interaction with our app based upon that authentication?

When a user is authenticated, a flag is set on the user object. We can control
views based on that flag.


```python
def some_view(request):
    user = request.user
    if user.is_authenticated:
        # do something
    else:
        # do something else
```

**Every logged-in user is authenticated,** and every ` request` object has a
`user` attached whether or not that user has logged in. When the user hasn’t
logged in yet, the `user` object attached to `request` is an instance of the
[AnonymousUser](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser).
Amongst other things, `AnonymousUser.is_authenticated` is always set to
`False`.

## AuthN with Decorators

For every `view` that handles a route, we can check to see if the user is
authenticated the same way we have above to decide what they should and
shouldn’t be able to see. That, however, is not only repetitive but tedious.

Thankfully, `django.contrib.auth.decorators` equips us with the
`@login_required` decorator. This decorator **requires that the current user
be logged in** and authenticated in order to view the page.

We can set as an argument on this decorator the `login_url`. This will be the
location of the login page in case the current user isn’t authenticated. This
way, when an anonymous user tries to access a route that requires
authentication, they get redirected to a login page instead.


```python
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def some_view(request):
    # do whatever you want
```

Of course, as the developer you always have control over the user’s
interaction with _your_ app. You don’t **have** to allow them an opportunity
to log in. You can just redirect them to a boilerplate ` 403 Forbidden` page.
All that would be different is the URI that you direct the user to with
`login_url`.


```python
from django.contrib.auth.decorators import login_required

@login_required(login_url="/forbidden/")
def some_view(request):
    # do whatever you want
```

## AuthN vs AuthZ

Often in the world of web development you’ll hear/read the term “ **auth-
auth** ”. This refers to Authentication (AuthN) and Authorization (AuthZ).
They both have a place when considering the security of your app. They refer,
however, to very different things.

As we’ve seen, **AuthN** just checks that the user is who they say that they
are. **AuthZ** on the other hand checks that the user is able to do what they
are trying to do.

It’s the difference between the ID card that verifies who you are and the key
that gets you in the locked doors. In Django, AuthZ is handled by the same
module that handles AuthN: `django.contrib.auth`. With it we can declare what
**permissions** a given user (or group of users) may possess. We can also
decide upon which permissions may be needed to access certain functionality.

For example, we might expect an `admin` to be able to delete our Books at
will. That’s part of what an admin _should_ do. However, should just any user
have that same ability?

If I set up a work environment for people from my company on a site like
Waffle IO or Trello, should non-affiliated users have access to reading or
writing privileges?

## How Does Django Grant Permissions (AuthZ)?

Django grants permissions to individual users and groups of users. It checks
permissions for actions on individual model instances, or actions within view
functions/classes. Let’s see how.

### Built-In Permissions

By default, Django has 3 types of permissions built-in: `add`, `change`, and
`delete` for **every model**.

Take, for example, our `Book` model. If we wanted to require that a user’s
ability to add/change/delete an book depends on permission to do so, we can
use the `permission_required` decorator like so:


```python
from django.contrib.auth.decorators import permission_required

@permission_required("lender_books.add_book")
def create_book(request):
    # things that create a new book object
```

You can also require that multiple permissions be possessed by a given user
for a given view. All you must do is provide an iterable of permission names.


```python
@permission_required(("lender_books.change_book", "lender_books.delete_book"))
def edit_book(request):
    # things that would either edit or delete a given book
```

If your user doesn’t have the appropriate permissions, they will get
redirected to the default Django login page. You can set a URL of your own
with the `login_url` kwarg, just like with the `@login_required` decorator.


```python
@permission_required(("lender_books.change_book", "lender_books.delete_book"), login_url="/")
def edit_book(request):
    # things that would either edit or delete a given book
```

### Creating New Permissions

The default permissions are great for basic functionality. We may however want
to require a permission that doesn’t yet exist. For example, we may restrict
the ability to view a certain portion of our app only to those with some
privilege.

The only way we’ve restricted viewability thus far is to require login for a
given view. However what about if we have authenticated users that shouldn’t
be authorized to do certain things? We need to create new permissions.

We can create custom permissions for a given `Model` by altering the
`permissions` attribute on the model’s `Meta` class.


```python
class Book(models.Model):
    ...
    class Meta:
        permissions = (
            ("view_book", "Can see books"),
        )
```

This new permission will get created once you make migrations and migrate.
After the migrations are in place, you will be able to block out users without
the `lender_books.view_book` permission.

### Adding User Permissions

It’s great to be able to create new permissions, but you need to also give
users these new permissions. Otherwise, we have all these great restrictions
without any users that can bypass them. To add permissions to an individual
user, you’ll have to manually add that permission.


```python
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

perm = Permission.objects.get(name="Can see books")
bob = get_user_model().get(username="bob")
bob.user_permissions.add(perm)
```

You can do this on registration or after some other sequence of tests for a
given user, but that’s tedious. It makes more sense to have a `Group` of
authorized users that you then add users to. You can then control permissions
for that entire group at once.

Django allows you to control groups within the Django Admin. The `Groups`
panel lets you manage groups by adding or editing existing ones, choosing
which permissions a given group should be allotted. You can then go into the
`Users` section of the panel to add a given user to a Group, thereby managing
permissions for many with one single heading.

### AuthN with AuthZ

There’s no reason why you should only have _either_ AuthN _or_ AuthZ for a
given view. Stack your decorators!


```python
@login_required
@permission_required(("lender_books.change_book", "lender_books.delete_book"))
def edit_book(request):
    # things that would either edit or delete a given book
```

That way, you not only check that a user is logged in. You also that your
authenticated users have the appropriate permissions.

Granted, only authenticated users have permissions, so you could probably just
get away with `@permission_required`.

## Auth-Auth in Class-based Views

Of course you may not even use function-based views. If you only use class-
based views, those decorators are now useless. You can however use Django’s
mixins to add the same functionality to those views.

Consider this view to access a book.


```python
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

class BookDetail(PermissionRequiredMixin, DetailView):
    permission_required = "lender_books.view_book"
    # other relevant things
```

By including the `PermissionRequiredMixin` in your inheritance list, you have
access to functionality similar to that of the decorator on the function-based
views.

You can provide individual permissions or an iterable of permissions. You can
specify the `login_url` as before, just as a class attribute. You also have
access to the `handle_no_permission()` class method, which you can override to
do something special to handle users without permissions.

Similarly there’s a `LoginRequiredMixin`, which provides just the `login_url`
class attribute and some authentication. When a user isn’t authenticated,
they’re redirected to that URL.

## Security at View/Template Interface

App security can be enforced not only at the `Controller` level in your Django
views, but in the templates as well.

### Escaping Text

One way in which users can abuse each other is via `Cross-Site Scripting
(XSS)`. With XSS, one user will set up some malicious JavaScript and submit
that to your app’s database. If that user’s data gets read out and viewed
somewhere else, whoever views that code will run that user’s JavaScript. They
would then become a victim of whatever that code is meant to do. This can mean
a redirect, stealing cookies, or some other malicious activity.

You can prevent malicious code harming your users at large in two ways:

  * by **escaping** whatever text is submitted through your site’s forms.
  * by escaping whatever text is read from your database.

To escape text coming in from a form, use Django’s
[escape](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#escape)
filter


```python
from django.utils.html import escape
cleaned_body = escape(form.cleaned_data["text_field"])
```

This filter will convert quotes, ampersands, and angle brackets into [HTML
entities](http://www.w3schools.com/html/html_entities.asp). These entities,
though they may still look like valid code, won’t run any JavaScript or other
malicious code embedded within HTML.

Similarly, you can escape any user input that comes from your database with
the escape template filter.


```jinja
<body>
    <div>
        {{ body_text | escape }}
    </div>
</body>
```

It’s not fool proof, but it will render most potential attack vectors like `<script>` tags to be harmless. It’s still entirely possible for an attacker to
use in-line JavaScript, and if you suspect that may occur you can enforce more
strict escaping rules.

### CSRF and Security Tokens

Consider the following form:


```html
<form method="post" action="my_info.html">
    <p>
        <label for="food">Favorite Food?</label>
        <input type="text" name="food" />
    </p>
    <p>
        <label for="school">Where Did You Attend High School?</label>
        <input type="text" name="school" />
    </p>
    <p>
        <input type="submit" value="Submit" />
    </p>
</form>
```

Where does this form post data, and what data does it post? If the destination
page actually existed, then anytime that I submit this form I’d be altering
that website’s data.

What about this form?


```html
<form method="post" action="https://onlinebanking.becu.org/BECUBankingWeb/af(kxjASs6RpWPzapPShB2v)/Transfers/AddTransfer.aspx">
    <p>
        <label for="source_acct">Source Account: </label>
        <input type="number" name="source_acct" value="1234567890"/>
    </p>
    <p>
        <label for="dest_acct">Destination Account: </label>
        <input type="number" name="dest_acct" />
    </p>
    <p>
        <label for="frequency">Frequency: </label>
        <select name="frequency">
            <option value="single" selected="selected">One Time</option>
            <option value="weekly">Weekly</option>
            <option value="biweekly">Every Two Weeks</option>
            <option value="monthly">Monthly</option>
            <option value="quarterly">Quarterly</option>
            <option value="annually">Annually</option>
        </select>
    </p>
    <p>
        <label for="transfer_date">First Transfer Date: </label>
        <input type="text" name="transfer_date" />
    </p>
    <p>
        <label for="routing">Routing Number: </label>
        <input type="number" name="routing" />
    </p>
    <p>
        <label for="amount">Amount: </label>
        <input type="number" name="amount" />
    </p>
    <p>
        <input type="submit" value="Continue" />
    </p>
</form>
```

If this form was written correctly, matching the format that the destination
site expects, I could easily steal money from the given account and transfer
it wherever I wanted. Many people’s information has been stolen this way, and
victims have lost millions from this practice of **Cross Site Request
Forgery**.

One way to combat against this is to authenticate any form submitted to your
website. Ensure that the form submission came from your website, and goes to
somewhere else in your website that expects that form. Furthermore, ensure
that the form is authentic and is a one-time submission only.

Django allows you to handle this easily with the `{% csrf_token %}` template
tag. This adds a hidden field to your form submission containing a unique
cookie, generated at the time of submission. Your web app expects to see this
hidden field, with a unique value specifically generated by your individual
submission.

To include a CSRF token in your form, just add the template tag.


```html
<form method="post" action="my_info.html">
    {% csrf_token %}
    <p>
        <label for="food">Favorite Food?</label>
        <input type="text" name="food" />
    </p>
    <p>
        <label for="school">Where Did You Attend High School?</label>
        <input type="text" name="school" />
    </p>
    <p>
        <input type="submit" value="Submit" />
    </p>
</form>
```

