# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 17: Pyramid - Authentication

## Pyramid: Connect Models to Views

**This is a solo assignment**

We're continuing to build the stock portfolio application.

### Specifications

- In your `pyramid-stocks` repository create a branch called `class-17-authentication`
- Create a new file in the root of your project called `security.py`
- In `security.py`:
    + Configure a root factory for your ACL rules, which provide the ability for anyone to `view` a route and another which dictates that a route is protected or `secret`.
    + Define an `includeme` function for the applications `Configurator` to recognize and mount up when the application starts.
        * This should take care of setting AuthN and AuthZ policies, mounting your root factory, and setting the default `csrf` options to true.
- In the applications root `__init__.py`:
    + Add `security.py` to the configuration.
- Modify your views in the following ways:
    + Whenever a `GET` request is sent to your auth view...
        * on success, redirect the user to their portfolio view
        * if the user is already logged in, redirect them to their portfolio view
        * if the user isn't already logged in, show the auth forms
        * if the authorization fails (malformed request data), return an appropriate exception to the user
    + Whenever a `POST` request is sent to the auth view...
        * on success, redirect the user to their portfolio view
        * if the account already exists, return an appropriate exception to the user
        * if the authorization fails (malformed request data), return an appropriate exception to the user

    + Ensure that an unauthenticated user, trying to access the following routes, is redirected to the auth view:
        * `/stock`
        * `/portfolio`
        * `/portfolio/{ticker}`

### Testing
- Ensure that both your views and models have been thoroughly unit tested. You should have at least three tests for each view controller, as well as each model. Your coverage reports should guide you to line coverage, and your goal is 80% or better in your coverage reports.

### Submission

1. Create a pull request from your `class-17-authentication` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-17-authentication` into `master`

---

## Project Prep: Write User Stories
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
