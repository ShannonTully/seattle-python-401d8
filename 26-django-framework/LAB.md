# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 26: Django Imager: Create the Imager Profile

## Django Imager: Create the Imager Profile

In this series of assignments you will build a simple image management website using Django.

**This is a paired assignment**

### Specifications

- Create a new repository called `django-imager`, and add your partner as a collaborator. Set it up with a Python `.gitignore` and a MIT license
- Clone your project and create a new virtual environment within. pip install the latest version of Django into your environment. Set up a `requirements.txt` file and a basic README.md and commit these changes to master.
- In your `django-imager` repository create a branch called `class-26-profile`
- Once the branch is created, start a new Django project using the `django-admin`. Call the project `imagersite`. Add the structure created by Django to your repository and commit the changes to your branch.

You’ll be creating your first data model for a simple photo management application.

#### User Profile
We will begin with users. Django has a full-featured user system, but we want a few more bits of data about our users. Users of our application will have a profile that captures information about each user not directly related to authentication. The Django way is to organize individual units of functionality in a website into “apps”. Our user profile is just such a unit.

Create a new app by changing directories into the `imagersite` folder you created above. You should be in a folder with a file called `manage.py`. Build a new app using that management command file and call it `imager_profile`. The model for our user profile will be contained in this app.

Your `ImagerProfile` model must support the following API:
```python
    # This is a package that needs installation; don't forget to add it to your requirements.txt
    from multiselectfield import MultiSelectField

    user = models.OneToOneField(User, related_name='profile')

    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    website = models.URLField(max_length=180, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    camera = models.CharField(max_length=180, blank=True, null=True,
                              choices=(('DSLR', 'Digital Single Lens Reflex'),
                                       ('M', 'Mirrorless'),
                                       ('AC', 'Advanced Compact'),
                                       ('SLR', 'Single Lens Reflex')))
    services = MultiSelectField(
        choices=(('weddings', 'Weddings'),
                 ('headshots', 'HeadShots'),
                 ('landscape', 'LandScape'),
                 ('portraits', 'Portraits'),
                 ('art', 'Art')))

    photostyles = MultiSelectField(
        choices=(('blackandwhite', 'Black and White'),
                 ('night', 'Night'),
                 ('macro', 'Macro'),
                 ('3d', '3D'),
                 ('artistic', 'Artistic'),
                 ('underwater', 'Underwater')))
```
- `ImagerProfile.active`: provides full query functionality limited to profiles for users who are active (allowed to log in)
- `profile.is_active`: a property which returns a boolean value indicating whether the user associated with the given profile is active

Ensure that each of your models has a string representation that appropriately displays it when using the Django shell.

You must ensure that if a user is deleted from the database, the `ImagerProfile` associated with that user is also deleted.

Create migrations to support installing your new app. We may or may not have discussed Django migrations in class. Regardless, if you need a reference, check the Django [documentation](https://docs.djangoproject.com/en/2.0/topics/migrations/) on migrations. You will not be able to save Model instances to your database without migrations!

Create a default app configuration to handle configuring a few global settings for the app.

### Testing
You will implement tests that demonstrate the API you have implemented. Use Django’s built-in testing systems and the Test Case classes it provides. Ensure that the tests demonstrate all aspects of the functionality, including access control. As demonstrated in class, use `FactoryBoy` to create any required objects your tests need to run properly.

### Submission

1. Create a pull request from your `class-26-profile` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-26-profile` into `master`

---

## Implement a K-ary Tree

**This is a solo assignment**

### Specifications
- Create a new branch in your `data-structures-and-algorithms` repository called `k-tree`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Create a new directoruy called `k_tree/`, with all of your standard module configuration for each directory
    - `__init__.py`, `README.md`, etc.
- Create a file called `k_tree.py`, as well as a test file and a config file for your tests.

- In `k_tree.py`:
    - Create a Class or a `Node` which is aware of the value as `val` and children as a list collection of Nodes
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the node
    - Create a Class for a `KTree`, which is aware of the root of the tree as `root`
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the tree
        - This class should be aware of depth-first traversal methods for `pre_order`, and `post_order` traversals
        - This class should be aware of a breadth-first traversal method
        - This class should have the ability to `insert` a new node into the tree at a given parent node

- Ensure that your class and any subsequent methods are properly tested, and that your test coverage is above 80%.


### Submission
1. Create a pull request from your `k_tree` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `k_tree` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
