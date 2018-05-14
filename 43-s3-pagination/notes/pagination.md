# Django Pagination

## What is Pagination?

Pagination offers the ability to spread all of your results across multiple
pages. For example, consider a blog with 10,000 posts. If my home page lists
all of my blog posts, it’ll show entirely too many to be seen by one viewer.
So we split them into pages, showing 5 or 10 per page.

Most frameworks contain some method for paginating query results. Django is no
different.

## The Django Paginator

The Django `Paginator` object is part of the Django core. In fact, it is
imported from: `django.core.paginator`.

    
```python
from django.core.paginator import Paginator
```

In order to use the `Paginator` object, you must pass as the first argument a
`QuerySet` object.

Let’s take for example the `PatronProfile` model from our Django Lender app.
If we have more than one user, then we’ll have more than one profile to work
with. If we were building our Django Lender into a full
[Goodreads](https://www.goodreads.com/) clone, then we’re going to have a lot
of users to work with. As an admin, you may want to list all the current users
for some reason. To get them all you’d write something like the following.

    
```python
from patron_profile.models import PatronProfile

all_profiles = PatronProfile.objects.all()
```

`all_profiles` now contains a `QuerySet` containing all of the available
PatronProfile model instances. I can access these model instances in pages
with one instance each using `Paginator`.

    
```python
paginated = Paginator(all_profiles, 1)
profiles = paginated.page(3)
```

**Pages are not zero-indexed**. They follow human counting, starting at 1.

Let’s inspect `profiles` a sec.

    
```
In [1]: type(profiles)
Out[1]: django.core.paginator.Page
```

Even though `profiles` holds one page of profiles (in this case, only one),
it’s just a `Page` object, not a `PatronProfile` instance.

To access the actual objects held within each page, we must use the
`object_list` attribute.

    
```
In [2]: profiles.object_list
Out[2]: <QuerySet [<PatronProfile: Bob Bobberton>]>
```

`object_list` contains a QuerySet! What else does `profiles` contain?

```
In [3]: dir(profiles)
Out[3]: [ # a bunch of special methods 'count', 'end_index', 'has_next', 'has_other_pages', 'has_previous', 'index', 'next_page_number', 'number', 'object_list', 'paginator', 'previous_page_number', 'start_index']

In [4]: profiles.has_next()
Out[4]: True

In [5]: profiles.has_previous()
Out[5]: True
```

Experiment to your heart’s content. Let’s include this in some function-based
views though.

## Pagination in Function-based Views

There’s not much going on here that’s very unusual given what we’ve done
already. We already know how to make a list view. The only things we do
differently here are reduce the number of items we show at one time, and
handle the paging itself.

Let’s write ourselves a simple list view.

    
```python
from django.shortcuts import render
from patron_profile.models import PatronProfile

def list_profiles(request):
    """List all of the available user profiles, page by page."""

    all_profiles = PatronProfile.objects.all()
    return render(request, "profile_list.html", {"profiles": all_profiles})
```
  

We want to paginate our user profiles. Let’s start by initializing a
`Paginator` object showing 2 items per page.

    
```python
from django.core.paginator import Paginator
from django.shortcuts import render
from patron_profile.models import PatronProfile

def list_profiles(request):
    """List all of the available user profiles, page by page."""

    all_profiles = PatronProfile.objects.all()
    pages = Paginator(all_profiles, 2)
    profiles = pages.page(1)

    return render(request, "profile_list.html", {"profiles": profiles})
```
  
We start by default getting the first page of items. We then return **only
those items that exist in that page**. Note: we don’t actually need to pass in
the ` object_list` attribute and actually it works out better for us if we
don’t.

We can have our simple template that just lists the profile names.

    
```jinja
{% extends layout.html %}
{% block content %}

<ul>
{% for profile in profiles %}
    <li>{{ profile.user.first_name }}</li>
{% endfor %}
</ul>

{% endblock %}
```

Our rendered HTML will look like so:

    
```html
<!-- Stuff from the layout -->

<ul>
    <li>Melissa</li>
    <li>John</li>
</ul>

<!-- Stuff from the layout -->
```

If we instead choose a different page, we get different results:

    
```python
# Python

from django.core.paginator import Paginator
from django.shortcuts import render
from patron_profile.models import PatronProfile

def list_profiles(request):
    """List all of the available user profiles, page by page."""

    all_profiles = PatronProfile.objects.all()
    pages = Paginator(all_profiles, 2)
    profiles = pages.page(2)

    return render(request, "profile_list.html", {"profiles": profiles})

```
```html
<!-- Stuff from the layout -->

<ul>
    <li>Amy</li>
    <li>Kelly</li>
</ul>

<!-- Stuff from the layout -->
```

## Pagination with Controls

What fun is pagination if you can’t actually change the page? We won’t have to
make a new route for this though, we can just use query parameters from the
`GET` request itself.

If, for example, the route to our profiles list is `/patrons`, then the URI
for our paged `GET` request will look like `/patrons?page=2`.

We can use that to empower our list view to handle pages.

    
```python
from django.core.paginator import Paginator
from django.shortcuts import render
from patron_profile.models import PatronProfile

def list_profiles(request):
    """List all of the available user profiles, page by page."""
    all_profiles = PatronProfile.objects.all()
    this_page = request.GET.get("page", 1)

    pages = Paginator(all_profiles, 2)
    profiles = pages.page(this_page)

    return render(request, "profile_list.html", {"profiles": profiles})
```
 
Now, whenever the `/patrons` route is hit with the `page` query parameter
equal to some number, we return that page of results.

We can alter our template to give us links to all of the available pages of
user profiles. `profiles.paginator.page_range` gives us a range of numbers
starting at 1 and ending at the last page we have. We can use that in a `for`
loop to print out all our available pages.
   
```jinja
{% extends layout.html %}
{% block content %}

<ul>
{% for profile in profiles %}
    <li>{{ profile.user.first_name }}</li>
{% endfor %}
</ul>

<nav>
    <ul>
    {% for page_num in profiles.paginator.page_range %}
        <li><a href="?page={{ page_num }}">Page {{ page_num }}</a></li>
    {% endfor %}
    </ul>
</nav>

{% endblock %}
```
  

Now clicking on any one of those links will send us to that page of items.

This is great to start, but we must handle some edge-cases. What should happen
if a value is provided that is negative, or outside of the range of pages?
What should happen if a value is provided that isn’t even a number?

### Handling the Edge Cases

`django.core.paginator` comes equipped with two useful custom exceptions:

  * `PageNotAnInteger`: when the value provided to “page()” isn’t an integer
  * `EmptyPage`: when the requested page has no results

They both inherit from paginator’s `InvalidPage` exception class.

    
```
>>> from django.core.paginator import EmptyPage
>>> EmptyPage.__mro__
(django.core.paginator.EmptyPage,
 django.core.paginator.InvalidPage,
 Exception,
 BaseException,
 object)
```

With these in hand, we can add a `try-except` block to handle these edge-cases
and return something we think should be relevant to the user.

Let’s say that in the event we’re given completely-invalid input, we return
the first page. If we get a page number outside of our actual page range, we
return the last page.

    
```python
# other imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list_profiles(request):
    """List all of the available user profiles, page by page."""
    all_profiles = PatronProfile.objects.all()
    this_page = request.GET.get("page", 1)

    pages = Paginator(all_profiles, 2)

    try:
        profiles = pages.page(this_page)
    except PageNotAnInteger:
        profiles = pages.page(1)
    except EmptyPage:
        profiles = pages.page(pages.num_pages)

    return render(request, "profile_list.html", {"profiles": profiles})
```

## Pagination with Class-based Views

Pagination is quite simpler with class-based views. The bulk of the work gets
pushed toward the template instead of the view itself.

   
```python
from django.views.generic.list import ListView
from patron_profile.models import PatronProfile

class ProfileListView(ListView):
    """Class-based view for my list of user profiles."""
    model = PatronProfile
    template_name = "profile_list.html"
    context_object_name = "profiles"
    paginate_by = 2
    queryset = PatronProfile.objects.all()
```
  

  
My template will now look a little different.

    
```jinja
{% extends layout.html %}
{% block content %}

<ul>
{% for profile in profiles %}
    <li>{{ profile.user.first_name }}</li>
{% endfor %}
</ul>

<nav>
    <ul>
    {% for page_num in paginator.page_range %}
        <li><a href="?page={{ page_num }}">Page {{ page_num }}</a></li>
    {% endfor %}
    </ul>
</nav>

{% endblock %}
```

## Wrap Up

Pagination is a great way to use Python to control the user experience. No one
wants to be inundated with every last object you have in your database. Let
the user choose the experience that they want with the controls that you set
out.

We’ve seen a way for adding pagination to our Django app. Now let’s implement
pages for images, albums, and images belonging to albums. Don’t forget to test
that the Pagination works, as well as the edge cases!

