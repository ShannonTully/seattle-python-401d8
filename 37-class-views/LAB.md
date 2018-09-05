# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 36: Django Imager: Create Views to Add Models

## Django Imager: Create Views to Add Models

In this series of assignments you will build a simple image management website using Django. In this fifth step, you will provide users with a way to add resources from the front-end of the application. That way, you need not grant them access to the Django admin.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-36-class-views`

**BEFORE YOU START ANY OF THE NEW VIEWS BELOW** , convert your existing function-based views to be **class-based views.** Instead of going generic and using the ` TemplateView`, do what you can to try and use a more specific CBV. The right CBV for the right job.

#### Creating
  * Construct views that allow the creation of `album` and `photo` instances.
  * From the `library` page you created previously, add prominent buttons that allow for easy navigation to the `album` and `photo` creation pages.
  * Each creation page should show a form with the needed fields to create a new album or photo.
  * The `album` form need not offer the ability to upload photos. Only assign photos that already exist.
  * When the form is submitted, the user should be redirected to the `library` page where they can see the newly created object.

The URLs for these pages should be

  * `/images/albums/add/`
  * `/images/photos/add/`

### Testing

* You must implement tests to ensure your views are functioning properly. As an example, a user should not be able to create a photo or album with any required field missing.

### Submission

1. Create a pull request from your `class-36-class-views` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-36-class-views` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
