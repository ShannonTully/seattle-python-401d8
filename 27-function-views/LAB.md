# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 27: Django Imager: Registration, Login and Home

## Django Imager: Registration, Login and Home

In this series of assignments you will build a simple image management website using Django. You began by defining a data model. Next, you’ll create a home page, and allow new users to register for an account.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-27-registration`

#### Styling
Unless you have strong opinions about design, you can get a reasonably nice-looking design using a front-end framework like Bootstrap or Zurb Foundation. There are good add-ons available for both (django-bootstrap3, django-zurb-foundation). In any case, put some effort into making your `base.html` look nice, whether you choose to use a framework for that or not. Note that Django templates use inheritance in the exact same way as Jinja2. Use `base.html` as your layout skeleton, and have your other templates inherit from that.

#### Home Page
The home page for your application should have the url `/`. It will contain marketing text that invites users to join the site. It will include a prominent display of an image chosen at random from all the public photos uploaded by your users. For the moment there are no public photos, so it should show an image you pre-select (served as a static resource) instead. Check [these docs](https://docs.djangoproject.com/en/2.0/howto/static-files/) for information on how to serve up static resources.

In addition to the above elements the page will provide clear calls to action for logging in or joining the site. The login call to action, when clicked, will lead to a login form. The registration call to action will lead to the registration page.

The home page should make use of a basic HTML skeleton provided by a `base.html` template. It should fill blocks in that skeleton rather than defining the entire layout of the page itself.

#### Login / Logout
The site will allow users to log in and out of the system without needing to go to the Django admin login page. The urls for these views will be `/login` and `/logout`. I encourage you to use the views already provided by the `django.contrib.auth` package for login and logout rather than creating your own. You can override the view template used for login to make it extend your `base.html` skeleton template.

A successful login will try to redirect the user to a route called `/accounts/profile`. For now, enable your Imager app to redirect to the home page instead. To do this, create a `LOGIN_REDIRECT_URL` in your `settings.py`. It should be a simple string pointing to a route that is registered and exists in your app, like `/profile` or `/images/library`.

#### Registration
The site will allow new users to register themselves so as to begin using the service. To make this work, you will install and configure a Django add-on called [django-registration](http://django-registration.readthedocs.io/en/stable/). It provides all the required functionality.

You will need to add the URLs for the application to your site urlconf. You will also need to provide all the required templates. You will use the HMAC registration backend which uses the following registration flow:

- Users fills out registration form and clicks ‘submit’
- User ends up at a page that informs them that an email has been sent to them with a link to finish the registration.
- User clicks on the link in the email and ends up at a page that tells them that their registration has been confirmed.
- User can then log in to the site with the username and password they provided when they registered.

Once a user logs in, they should be redirected to the home page, but they should now see their username in the top left corner of the page.

Because the registration service involves sending emails, you will have to configure [email services for Django](https://docs.djangoproject.com/en/2.0/topics/email/). However, you don’t want to send real emails when developing, so make sure that you configure the [Django console email backend](https://docs.djangoproject.com/en/2.0/topics/email/#configuring-email-for-development). Then any emails you send while working will simply print to the console where Django is running.


### Testing
- You must write tests for each view you implement, verifying that it works as expected. Since these tests will involve rendered html you will want to read about the [Django test client](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#the-test-client).

- STRETCH: To test registration you will want to be aware of how [Django’s email services work in a test environment](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#email-services).

### Submission

1. Create a pull request from your `class-27-registration` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-27-registration` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
