# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 28: Django Imager: Create Photo and Album Models

## Django Imager: Create Photo and Album Models

In this series of assignments you will build a simple image management website using Django. In this third step you will implement new models specific for viewing and handling images on your site.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-28-relationships`

#### Image Management
The main functionality of our application will be oriented around uploading and organizing images. Our second Django app will encompass the models and views associated with this work.

From the root of your project, where the manage.py file is located, create a second app called `imager_images`.

You’ll need to create two models in this new app, the `Photo` and the `Album`.

#### Photos
Photo represents an individual picture uploaded by a user. It will contain the image file itself, plus metadata about that file. One Imager user can own several photos, but photos themselves are owned by a single user. Meta-data should include `title`, `description`, `date_uploaded`, `date_modified`, and `date_published` fields. You should also have a `published` field which takes one of several possible values: (‘private’, ‘shared’, ‘public’)

#### Albums
Album contains Photo instances and provide meta-data about the collection of photos they contain. Any one album must be owned by a single `User`. Any album can contain many Photos and any Photo may be in more than one Album. Meta-data should include an album `title` and `description`. It should also contain a `date_created`, `date_modified`, and `date_published` as well as a `published` field containing the same options described for Photos. Users should be able to designate one contained photo as the cover for the album.

#### DB Migrations
Create migrations to support installing your new app.

Create a default app configuration to handle configuring a few global settings for the app. Don’t forget to include your models in the Django admin.

#### Testing
Finally, you will implement tests that demonstrate the API you have implemented. Use Django’s built-in testing systems and the Test Case classes it provides. Ensure that the tests demonstrate all aspects of the functionality.

Use FactoryBoy to create any required objects your tests need to run properly.

### Submission

1. Create a pull request from your `class-28-relationships` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-28-relationships` into `master`

---

## CSS Code Challenge

**This is a solo assignment**

For this CSS code challenge, you will develop code that renders an elevator panel that  matches the [provided mockup](./assets/elevator.png).

You will then be adding JS code to make the elevator panel function according to the functional requirements below. You can control which way the elevator moves by selecting the ?floor? buttons on the panel. As soon as a button is selected, the elevator will begin moving toward that floor.

### UI Requirements:
- A display panel that indicates the number of the current floor
- Green and red lights indicating whether the elevator is going up (green) or down (red)
- Four floor buttons
- Four floors behind the elevator panel, represented as images you select from any free source on the internet

### Functional Requirements:
- A floor can be selected from the elevator panel.
- When a floor is selected, its button is highlighted.
- Clicking on a floor button in the panel will cause the floors in the background to scroll up and down.
- Multiple floors can be selected and will be executed in the order that they were selected.
- The chosen button should remain highlighted until the floor is reached.
- The current floor is shown on the display panel. (This is the large number on the panel display.)
- The elevator's current direction (up/down) is indicated by highlighting the corresponding  green and red indicators in the display panel.
- A visual cue is provided when you have arrived at the selected floor. (Un-highlight the button, deactivate the direction indicators, and update the displayed floor.)
- Selecting a button anchor does not navigate or change the URL.

### Submission
1. Create a new repository called `ui-challenges`
1. Create a pull request from your `elevator-panel` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `elevator-panel` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
