# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 37: Django Imager: Forms & Security

## Django Imager: Forms & Security

In this series of assignments you will build a simple image management website using Django. In this sixth step, you will provide users with a way to edit resources from the front-end of the application. Now you’ll be able to interact with your site fully from the front end.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-37-edit`

#### Editing

Create views that allow updating existing albums and photos. On the `library` page, add an `edit` button to each album and photo that will load this view when clicked. The view that loads should show a form with the fields of the object to be edited. The album form should offer the user the ability to choose photos from their library to add to the album. When the form is submitted, the user should be returned to the library page.

The URLs for these pages should be

  * `/images/albums/<album_id>/edit/`
  * `/images/photos/<photo_id>/edit/`

Finally, create a view that allows a user to edit their `Profile`. This view should provide access not only to the data on the user’s ImagerProfile, but also to fields like `email` or `first_name` and `last_name` that are defined on the `User` object instead. When the form is submitted, the User should be returned to their `profile` page where they can see the updated information.

The URL for this page should be `/profile/edit/`

### Testing

* You must implement tests to ensure your views are functioning properly. In particular ensure that no user may edit resources that do not belong to him or her.

### Submission

1. Create a pull request from your `class-3-edit` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-3-edit` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
