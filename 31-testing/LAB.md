# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 31: Django - Testing

## Django - Testing

Today is all about testing your application. You'll have an opportunity to clean up code, style your templates, and fully test your Django application.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-31-testing`
- Ensure that you've taken the time to style your application. A polite reminder that styling is part of your job description; at least right now.
- Your base template should have a clean header and footer rendered for each page.
- Considerations for the User experience should be taken into account. For example, do not show a `logout` option for users who are not authenticated.

### Testing
- For each component of your Imager project:\
    + Write at least three unit tests for each view function you've written. Take care to not write tests for code that you did not write; (i.e. No need to test the User model that Django provides).
    + Write at least three unit tests for each model that you've defined as part of the application.
    + Write at least three functional tests for each route that you've defined as part of the application.
        - Ensure that all of your valid and invalid status codes have been tested, in addition to the actual response bodies for each.
- Configure a Travis-CI hook on your repository and ensure that your project is running tests in that environment anytime you push, PR, and/or merge into the Master branch.


### Submission

1. Create a pull request from your `class-31-testing` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-31-testing` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
