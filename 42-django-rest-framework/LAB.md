# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 41: Django: Implement a REST API for Imager

## Django: Implement a REST API for Imager

Django Rest Framework provides a full-featured framework for creating RESTful APIs based on the Django models you create. These APIs can then be used to power applications written for mobile devices, Javascript apps in Angular or other MVC frameworks, or even “normal” web apps, replacing the more traditional “view”-based approach to CRUD operations.

For your final assignment for the Imager app, you’ll be adding a RESTful API to expose a user’s photos for convenient download.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-41-drf`

Install Django Rest Framework into your virtualenv. Make sure to update your requirements.txt file. Then create a new app in your project folder. Call it `imager_api`.

In this app you’ll create one RESTful endpoint, a list of all photos belonging to a user. Each photo should include all metadata about the photo and a link to the image itself suitable for downloading the image.

For a stretch goal, provide a two more api endpoints to serve a list of albums. Each album record should contain all the metadata about the album and a link to the second endpoint. The second endpoint should be the same as the list of photos above, except that it takes an album id as an argument and returns the list of the photos in that album only.

Connect the URLs for your API at `/api/v1`.

Clearly, a user should have to provide authentication to access this endpoint.

You can test your api using the shell command curl, or you can install a nice little python library called [httpie](https://github.com/jkbrzt/httpie). This library will provide an “http” command on the command line which will print out in very nice color the result of calling your api.

### Submission

1. Create a pull request from your `class-41-drf` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-41-drf` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
