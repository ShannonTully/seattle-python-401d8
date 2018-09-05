# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 38: Front-end Design

## Django Imager: UI/UX

In this series of assignments you will build a simple image management website using Django. In this sixth step, you will provide users with a way to edit resources from the front-end of the application. Now you’ll be styling your site in a professional format.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-38-scss`

#### Front-end Design
* Following the general guidelines of SMACSS principles, create a series of `*.scss` stylesheets for your application, beginning with a `base.scss`, `vars.scss`, and any other generalized stylesheets.
    - Convert your existing stylesheets into the above format.
* Withing each of your Django apps, you should also have localized `*.scss` stylesheets which are specific to those component appications.
* In order to process those stylesheets into `*.css` static files, you will be implementing the`django-sass-processor` package found [HERE](https://github.com/jrief/django-sass-processor).
    - Follow the installation instructions, and then further the setup instructions on GitHub to set up and provide a processor for your application's stylesheets.
    - Ensure that you've followed the instructions all the way through understanding how this package enables collection of static assets for production deployment; i.e. what you've been familiar with as `collectstatic`.

### Testing

* If you're still lacking in unit and integration tests for your application, continue working on those today as well.

### Submission

1. Create a pull request from your `class-38-scss` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-38-scss` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
