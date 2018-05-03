# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 34: Deploy the Imager app to AWS

## Deploy the Imager app to AWS

Deploy your imager application to AWS, using manual means. You should **seriously consider** reading [this blog post](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04) first and making sense of it.

**This is a paired assignment**

### Specifications

Here are the things you must incorporate to get it all working:
  * Create an EC2 instance
  * Install and configure nginx to proxy to Django, and to serve static and media files without proxying these requests to Django.
  * Set up gunicorn or waitress serving your Django app as an upstart process (see the gunicorn deployment docs for examples of how to do this).
    * Install GUnicorn or some equivalent wsgi server
    * Install your application code
    * Create an upstart conf file that includes required system environment variables to get everything working correctly.
  * Create an RDS instance and connect to it from Django.
  * Use a gmail account to send email. Be very careful about setting up an appropriate setting for DEFAULT_FROM_EMAIL. If this is not set to the address that belongs to the gmail account (or an alias registered with the account) google will refuse to send the email.

For a basic walkthrough of this process, [see this lecture](http://uwpce-pythoncert.github.io/training.python_web/html/presentations/session10.html). You may wish to add [dj-database-url](https://github.com/kennethreitz/dj-database-url) and [django-configurations](http://django-configurations.readthedocs.org/en/latest/) to your setup to simplify the job of using environment variables to manage sensitive configuration.

You will absolutely want to read the [Django Deployment Checklist](https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/) in order to get your Django configuration squared away for public deployment.

Please read [this blog post](http://bruno.im/2013/may/18/django-stop-writing-settings-files/) for another approach to controlling settings across environments (an alternative to django-configurations).

### Submission

When you have the deployment working, and I can register myself for the site and upload some pictures, submit the URL for your running site.

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
