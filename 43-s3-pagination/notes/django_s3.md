# Django and AWS Simple Storage System (S3)

Sources:

  * [Using Amazon S3 to Store Your Django Site’s Static and Media Files](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)
  * [Deploy a fault tolerant Django app on AWS – Part 2: Moving static and media files to S3](http://www.jorgechang.com/blog/howto-deploy-a-fault-tolerant-django-app-on-aws-part-2-moving-static-media-files-to-s3/)

Amazon’s Simple Storage System (S3) is a great way to store static or media
files for an application. The permissions are fairly easy to set, so you don’t
have to fuss with things like user permissions on an EC2 instance. The data
itself is stored in the cloud, so there’s little concern about storage issues
on the server that you’ve provisioned.

Also a benefit of cloud storage, these resources can be easily accessed by any
application that you desire as many times as you like. So, you can share
resources between load-balanced servers instead of keeping multiple copies of
the same data across your network.

Let’s dive in!

## AWS IAM and S3 Management and Configuration

### Create an IAM User

When using AWS it’s very easy to fall into the habit of using the root user
(i.e. your normal account) to run all your operations. You can provision new
EC2 instances, set up new RDS databases, even configure static file storage
all with the root user.

However, in practice, you won’t be the only person working on a given project.
Whether you work with a team on the same project, or are simply one maintainer
of a long-running project, it helps to have some credentials for AWS linked to
the project, and not so much to one individual user.

For this, we have the AWS IAM (Identity Access and Management) user system.
[AWS’s IAM](https://aws.amazon.com/iam/) users are accounts that are managed
by a root user’s account, but are not the root user directly. You control the
IAM user’s access to various functionality, including but not limited to
whether they even need to log in to use AWS’s various services. You can create
as many users as you like, and they’re no extra charge for your account. Only
their usage is charegd to your account.

More specifically for our own interests, you’ll need an IAM user’s credentials
for Django to access AWS’s Simple Storage System (S3).

To get started with creating and managing IAM users, sign in as the root user
to your AWS console and find the IAM service. Find the “Users” menu item on
the left sidebar, then click on the `Add User` button to add a new user.

#### Selecting a Username and Access Abilities

While you can create multiple users at once, we only want to add one user for
now. Type a `username` into the provided input field.

Now’s one of the more important points. We need to decide what type of access
this IAM user is going to have. **Programmatic access** lets you access all of
the various AWS services this IAM user can use via the command line or from
(surprise surprise) a program. Enabling programmatic access will provide you
with an access key ID and secret access key for AWS’s development tools. The
AWS Management Console access allows this user to be able to interact with
AWS’s services through the browser.

You don’t need both, but you do need one. For our specific purposes of
allowing Django to modify an S3 bucket, we’ll need programmatic access.

#### Setting User Permissions

Your user will need to have specific permissions set for their access to AWS’s
services. If you have a group of users that you’re trying to set up with a
shared set of permissions, you might want to either add the user to an
existing group, or create a new group for this user to be a part of.

However, **groups are not necessary**. You can attach existing permissions to
an individual user instead of including them as part of a group.

You can give this user whatever permissions you want for access to your AWS
services. The `AdministratorAccess` policy gives the IAM user full access to
everything. You can choose that if you want to. You can also restrict access
to only the service that you expect to be used, like the S3 service. For that,
there’s `AmazonS3FullAccess`. There’s no one “right” way to do things here, so
choose as you please. Just make sure that whatever permissions you select
allow full access to the AWS S3 service.

#### Acquiring the Access Keys

After successfully creating the user, you’ll be lead to the success page where
you can download the credentials for every user that you created. **You must
download these credentials here! You will not be given another chance!** Save
them someplace that won’t be in version control. These are access keys that
have some degree of privilege for adding or deleting data from your S3 data
store, so it’s important that they be kept in a private place.

### Creating an S3 Bucket

[AWS’s S3 service](https://aws.amazon.com/s3/) is a system for simple object
storage. You can think of it like a bucket for your stuff, accessible for
anywhere (depending on permissions you allow). At base, developers use S3 for
storing static and media files. However, you could use S3 as the basis for a
serverless website, hosting your HTML files as well! We won’t do that, but
you’ll typically find S3 on the front lines of any sort of serverless
architecture.

Navigate to the S3 service on AWS’s browser console. The URL should look
something like `https://console.aws.amazon.com/s3`. The first page that pops
up should list whatever S3 buckets your account currently has access to. It
may be empty. Such is life.

Create a new S3 bucket by clicking the `Create bucket` button. Set the
**Bucket name** to be whatever you like, as long as it resolves to a valid
domain name. It must also be a unique name across all of the AWS S3 buckets
that have ever existed.

The region that’s set should match the region within which your account
exists. If that region isn’t set, something like US West (Oregon) should work
just fine.

When you’re done setting the name and region, click **Create**. Yay, you’ve
created an S3 bucket!

#### The S3 Access Control List

Now that the bucket has been created, there’s a little configuration work to
be done. First, consider how we’ve been writing our Django apps thus far.
We’ve housed all of our static files in a `/static` directory, and our media
files in a `/media` directory. Django is going to expect these directories to
exist no matter where we host our files, and will be upset if they’re not
available. In your bucket then, create these folders with the **Create
folder** button so that Django will later be able to find them.

You’ll have to manage access to this bucket with the **Permissions** tab’s
**Access Control List**. Your root user will already be set up with full read
and write permissions to your bucket. That makes sense, your root user is the
one that created it.

If you want to, you can also add other users. In order to do that, you need to
know their user ID. Because our IAM user has full `AdministratorAccess`, we
don’t need to add it as a user to be managed on our S3 bucket.

We do, however, want anyone and everyone to be able to `read` our S3 bucket
objects. As such, in the **Manage public permissions** section we set the
access levels for Everyone to “read”.

#### The Bucket Policy

Although we’ve configured access to the bucket and its objects, we need to
still set a bucket policy that dictates what types of resources are accessible
and how. Bucket policies can be quite opaque as far as what to specify and how
to specify it. Fortunately, AWS has created a [policy generator](http://awspolicygen.s3.amazonaws.com/policygen.html) to make it
slightly easier.

Let’s generate for ourselves a policy that allows any user at all to read the
objects in our bucket.

  * Select the `S3 Bucket Policy` from the **Select Type of Policy** dropdown menu.
  * Add the **Effect** of ` Allow`.
  * Add the **Principal** of ` *` so that anyone can get objects from our S3.
  * Ensure the selected **Actions** are just the ` GetObject` action.
  * Input the **Amazon Resource Name** for your bucket.
  * It’ll simply be something like `arn:aws:s3:::<whatever_your_bucket_name_is>/*`
  * Click **Add Statement** to add this policy to the full policy that we’ll be generating.

The **Amazon Resource Name** (ARN) is kind of like AWS’s own internal uniform
resource locator. It gives you the address to a given resource, whether it be
an EC2 instance, an IAM user, or even an S3 bucket, which is what we used
above.

When you click **Add Statement** , the policy generator will clear itself.
That’s fine for us, because it leaves us prime for writing another policy
statement.

Let’s also allow our IAM user to execute any CRUD action on our S3 bucket. For
this, we’ll need to know the **ARN** for the user that we created. It’ll look
something like `
arn:aws:iam:::<some_id_that_is_you>:user/<the_specific_iam_user>`. You can
find it in the detail page for the individual IAM user that you created. If
you wanted to allow an entire group to share the same bucket policy, your ARN
would instead look something like
`arn:aws:iam:::<some_id_that_is_you>:group/<the_specific_iam_group_name>`

  * Fill the **Principal** field with your IAM user’s **ARN**. For example: ` arn:aws:iam::123456789876:user/test_user`
  * Check the **All Actions** checkbox so that your IAM user has full CRUD access to your bucket.
  * Specify in the **Amazon Resource Name** field the resources you want this to apply to. You want this to apply to the bucket itself and any folders within. You’ll want two values for this, separated by a comma: ` arn:aws:s3:::<whatever_your_bucket_name_is>`, `arn:aws:s3:::<whatever_your_bucket_name_is>/*`

Add that second statement, then click **Generate Policy** to generate the full
bucket policy that you need. The result will be a large-ish JSON blob. Copy
the contents, and paste it into your **Bucket Policy Editor**. Finally, save
the bucket policy and it’ll be applied to your bucket. Here’s an example of
what it should look like:

    
```json
{
    "Id": "Policy0000000000000",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt0000000000000",
            "Action": "s3:GetObject",
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::cf401-python-test/*",
            "Principal": "*"
        },
        {
            "Sid": "Stmt0000000000000",
            "Action": "s3:*",
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::cf401-python-test",
                "arn:aws:s3:::cf401-python-test/*"
            ],
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789876:user/test_user"
                ]
            }
        }
    ]
}
```

#### The CORS Configuration

CORS stands for **Cross-Origin Resource Sharing** , and is what determines
whether your application (sitting at one domain, maybe an EC2 instance, maybe
somewhere else) and your S3 bucket (sitting at a different domain no matter
what) can talk to each other and share resources.

A CORS configuration should have been populated for you when you initially set
up your bucket to allow for any origin to access your bucket’s resources.
It’ll look like some XML with fields for allowed origins, allowed methods, and
the amount of time in seconds the browser will cache an S3 response. As an
example:

    
```xml
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>60</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

If you wanted to restrict resource access for whatever reason or change the
cacheing time limit (above it’s 60 seconds, by default it’s 50 minutes), you
could manage that here.

If you’ve made it to this point, you should have all of the S3 configuration
that you might need for your Django application. Let’s walk into Django’s side
of things and get it wired up to talk to your AWS S3 bucket.

## Connecting Django to AWS S3

An important thing to note is that since we’ll be setting up the static url
dynamically, **your application should never have hard-coded urls to static
files!** Those staticfile urls should always be populated with the ` {% static
'path/to/resource.css' %}` template tag.

To start, we’re going to need two new Python packages, as setting up new means
for storing files can otherwise can be a headache. Go to your terminal and run
the following line of `pip`:

    
```sh
(ENV) $ pip install django-storages boto
```

[django-storages](http://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) is a package whose
only purpose is to be the go-between for Django and cloud storage systems like
AWS or Microsoft Azure. It sets up some configuration rules and objects that
are very useful to include in your `settings.py`.

[boto](http://boto.cloudhackers.com/en/latest/) is a direct interface between
Python and Amazon Web Services. With the proper credentials, you could use
`boto` to provision new web servers, set up new S3 buckets, and generally
manage any of your AWS configuration. For our purposes, `django-storages` will
leverage `boto` to interact with AWS S3.

In order to have Django interact with the `django-storages` API, we need to
include it in the list of `INSTALLED_APPS` in our `settings.py` file.

    
```python
# in settings.py
INSTALLED_APPS = (
    ...,
    'storages',
)
```

We’ll need to tell Django the name of our bucket so that when it stitches
together the static urls, the urls point to the right location. Create an
easily-recognizable section in your `settings.py` file that will handle all of
your AWS configuration. To that section, add in your bucket’s name, the access
key id for your IAM user, and that user’s secret access key. These are all a
part of the credentials that you downloaded earlier when you initially made
your IAM user.

    
```python
# Amazon Web Services Configuration
AWS_STORAGE_BUCKET_NAME = 'cf401-python-test'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
```

As with any other secret information **WE NEVER EVER EVER HARD-CODE SECRETS OR
PUT THEM IN SOURCE CONTROL!!!!** Instead, use environment variables to
populate those values.

    
```python
 # Amazon Web Services Configuration
AWS_STORAGE_BUCKET_NAME = 'cf401-python-test'
AWS_ACCESS_KEY_ID = os.environ.get('IAM_USER_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('IAM_USER_SECRET_ACCESS_KEY', '')
```

We can then build the S3 domain name based on the bucket name

    
```python
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
```

### Setting Up Static and Media Storages

Once we’ve gotten everything that we need from the AWS side, we need to be
concerned about our application and where it will locate/place files. Up until
this point, we’ve kept static css/js/image files in a local `static/`
directory and any user-uploaded files in a `media/` directory. However, we now
have AWS and need to change modes accordingly.

When Django is looking for static and media files to access from AWS, it uses
the `S3BotoStorage` object from `django-storages`. The source code for this
object can be found in `$VIRTUAL_ENV/lib/python3.6/site-
packages/storages/backends/s3boto.py`. Amongst the litany of other class
attributes, there’s a `location` attribute that is set using whatever was
defined at `AWS_LOCATION` in your `settings.py`. If you didn’t define that
variable, it defaults to an empty string, which would point to the root of
your bucket. What this means is that if we were to use this storage object for
both our static and media files, they’d both be using the same location, which
would just be the root of our S3 bucket.

**We do not want to mix our static and media files into the same buckets.**
That was the whole point of making separate directories in the S3 bucket in
the first place! So, we’ll have to override that parameter by making our own
storage objects.

In the same directory as `settings.py` create a new file. You could call it
anything you want, but `custom_storages.py` is fairly descriptive for what
we’re about to do. Within this file we’ll create two storage objects:
`StaticStorage` and `MediaStorage`. Their only purpose is to override the
`location` class attribute, and nothing more. If there were drastically-
different settings required for the locations of our static and media files,
we might change other attributes.

In `custom_storages.py` write the following:

    
```python
# in custom_storages.py...

"""Custom storage classes for static and media files."""
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    """Custom storage class for static files."""

    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    """Custom storage class for media files."""

    location = settings.MEDIAFILES_LOCATION
```

Each of these custom storage classes will use the `STATICFILES_LOCATION` and
`MEDIAFILES_LOCATION` that we will now define in our `settings.py`. Our
`STATICFILES_LOCATION` will be the path from the root of our S3 bucket to the
directory where our static files are located. We placed our `static` directory
in our S3 bucket’s root, so we only need to point to that.

    
```python
# in settings.py below the current AWS configuration

STATICFILES_LOCATION = 'static'
```

The storage object we want to use will be the one that we just made.


```python
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'django_lender.custom_storages.StaticStorage'
```

Finally, the URL for all of our static files will start with the actual
location of the `static` directory in our S3 bucket. This will be a
combination of our `AWS_S3_CUSTOM_DOMAIN` and our `STATICFILES_LOCATION`.

    
```python
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'django_lender.custom_storages.StaticStorage'
STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
```

We’ll do pretty much the same stuff for our media files with one exception

    
```python
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'django_lender.custom_storages.MediaStorage'
MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
```

For file uploads, `django-storages` will look for the `DEFAULT_FILE_STORAGE`
setting.

At the end of the day, all of your AWS S3 configuration should look like this:

    
```python
# AWS Configuration

AWS_STORAGE_BUCKET_NAME = 'cf401-python-test'
AWS_ACCESS_KEY_ID = os.environ.get('IAM_USER_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('IAM_USER_SECRET_ACCESS_KEY', '')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'django_lender.custom_storages.StaticStorage'
STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'django_lender.custom_storages.MediaStorage'
MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
```

## Last Bits

### Keeping Development Local

AWS S3 storage is spectacular and a great way to move past issues of serving
files locally. However, you may still want to develop stuff locally using
resources that are somewhat different from what’s available in production or
anywhere in the cloud. You may not want to send requests to your S3 bucket for
development or testing. For this, you can have environment-dependent settings.

When in development, we keep `DEBUG = True` so that when things inevitably
break we can see exactly what it was that broke and where it happened. We
remove this from production because it’s a gigantic security hole, so we can
always be guaranteed that in production our `DEBUG` setting will be `False`.
We can use this to add logic that effectively says: **when in development, use
whatever my static files are locally with the same old setup that I used to
have.** Once we’re in a production environment, access S3.

This is more straightforward than it sounds. `if...else` logic can concisely
save the day! If `DEBUG == True` use the old-style settings. Otherwise, use
the S3 settings.

    
```python
# AWS Configuration

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'cf401-python-test'
    AWS_ACCESS_KEY_ID = os.environ.get('IAM_USER_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('IAM_USER_SECRET_ACCESS_KEY', '')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'django_lender.custom_storages.StaticStorage'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'django_lender.custom_storages.MediaStorage'
    MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    MEDIA_URL = '/imgs/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

### Getting Existing Files into S3

As we know, remote data stores don’t simply populate themselves. Django takes
care of that fairly easily with `collectstatic`, where we just make sure to
run `./manage.py collectstatic` whenever we deploy. That’ll take care of the
static files.

What about media files? If you start your application off using S3 for file
storage it won’t be an issue, you’ll simply be uploading data to your S3
bucket from the first moment your site goes live. However, you won’t always be
so lucky to have started off on the right foot.

There exists a bash command called `rsync` which is great for syncing
directories between two different computers. There’s an extension of this for
syncing files between your local filesystem and AWS called `boto-rsync`. It’s
a `pip` installable Python package.

    
```sh
(ENV) $ pip install boto_rsync
```

Warning

YOU SHOULD ONLY NEED TO DO WHAT FOLLOWS ONCE.

On the EC2 instance(s) where your media files are currently stored, you’ll
need to run this command in the shell:

    
```sh
(ENV) $ boto-rsync /path/to/media s3://<your bucket name>/media -a <your AWS ACCESS KEY ID> -s <your AWS SECRET ACCESS KEY>
```

Your `media` directory will then be copied in its entirety up into your S3
bucket.

