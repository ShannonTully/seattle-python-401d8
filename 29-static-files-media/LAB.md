# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 29: Django Imager: Data Views

## Django Imager: Data Views

In this series of assignments you will build a simple image management website using Django. In this fourth step you will implement the user-specific views for the application. You will create a profile page, where a user can see their own profile information. You will add a library page, where a user can see all the albums they’ve created and the photos they’ve uploaded. And you will set up views for individual photos and albums.

**This is a paired assignment**

### Specifications

- In your `django-imager` repository create a branch called `class-29-views`

#### Home Page Revisited
Before today, we didn’t have photos that we could put into the home page. Now that our models are ready, we can add the randomized image display that belongs on the home page.

Alter your home page so that it displays a published image at random from all of the images that your users have uploaded. If there are no images, display one that you pre-select.

#### Profile Page(s)
Every profile page should provide quickly readable, clear information to the user about a given profile.

For the user’s own profile, show the user some helpful information about their own usage of the application. Give them a count of how many images they have uploaded and how many albums they’ve created. Differentiate the count between private and public photos/albums.

This page should also provide easy navigation links to the library page (or perhaps that should be a globally available navigation link).

Once this page exists, you should reconfigure your system so that this page is where a user lands when they log in to your site. You should also make the displayed name in the top right corner of the site a link that leads back to this page.

The url for the user’s own page should be `/profile`.

For the profile pages of other users, think about what information you might want to hide. What might be sensitive information? Display information that would be appropriate for public viewing, but reserve some of the best stuff for the user’s viewing on their own page.

The url for any other user’s page should be `/profile/<username>`.

#### Library Page
This page should provide a quick, thumbnail view for all the albums a user has created and all the photos they’ve uploaded. For albums, display a thumbnail of the ‘cover’ image selected for the album. If no cover image has been selected, display a default image (from site static resources). For all items the title should be displayed. You should save space by displaying small images (thumbnails) in a grid format.

To best accomplish this task, you’ll install another Django add-on application, [sorl-thumbnail](http://sorl-thumbnail.readthedocs.org/en/latest/). (You can also try out [easy-thumbnail](http://easy-thumbnails.readthedocs.org/en/latest/index.html), but I haven’t used that one myself) The add-on will allow you to easily designate dimensions for thumbnails and will handle creating appropriately sized copies of uploaded images for you. You **may use the database cache store when configuring this application**. Redis or memcached are much faster, but a lot more work to get going locally; deifnitely a stretch goal.

For an extra challenge (also a stretch goal) find and install a Javascript add-on that will allow you to click on any image and view a full-sized version in a “lightbox” overlay. (I’ve used and enjoyed `fancybox`)

The URL for this page should be `/images/library`

#### Album and Photo Views
Provide simple views for photos and albums.

The individual Photo view should display an appropriately sized rendering of the photo, perhaps with a lightbox feature to show the full-sized image. It should also display any metadata available about the photo. Its url should be `/images/photos/<photo_id>`.

The Photo gallery view should display all of the public photos that have been uploaded to your app. Its url should be `/images/photos`

The individual album view should display all the photos in a given album in a grid format (you might re-use the layout you created for the library view above). Each photo in the album should be displayed. The url should be `/images/albums/<album_id>`.

The Album gallery view should display all of the public albums contained within the app. They should appear as their cover images. Its url should be `/images/albums/`.

If you get frisky, you might look into jQuery-based gallery plugins like `galleria` to see if you can render the entire album as a gallery.

#### Testing
You must write tests for your views.

_Note:_ If you wish to test the javascript functionality of your lightbox add-on (NOT REQUIRED), you will need to work with a browser testing framework like `Splinter`.

### Submission

1. Create a pull request from your `class-29-views` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-29-views` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
