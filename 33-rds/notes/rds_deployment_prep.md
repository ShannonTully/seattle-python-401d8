# Amazon RDS and Deployment Prep

Up to this point we’ve been working solely in development mode. We’ve had a
local PostgreSQL database, local settings, all dealing locally. However, we
want to be able to put ourselves on the map by displaying the results of our
development efforts to the world.

For this, we’ve started using Amazon Web Services. Once it’s up and running,
it ends up being a pretty straight-forward way to deploy a website. We have
yet, however, to be able to deploy something as complex as a Django
application because we haven’t had access to a remote database. Until now.

## Provision an AWS RDS Instance with PostgreSQL

Amazon’s RDS (Relational Database System) prepares and deploys a machine whose
sole purpose is to serve as your relational database. You can decide which
type of SQL database you intend to use (MySQL, PostgreSQL, Oracle, etc) and
how large it should be. You set up the base credentials and who should be able
to access it.

Then... it sits there. A bucket waiting to be filled. Provided that you have
the proper credentials, it can then be used **just like any other database**.

In your dashboard, navigate to the RDS Dashboard. Here, you can look at which
database instances you have up and running. You can also force your
database(s) to back up, or be removed entirely.

Just like with the EC2 instances, you can **launch an RDS DB instance** by
clicking the big orange ` Launch a DB Instance` button.

Since we’ve been using `PostgreSQL`, **choose the Postgres database engine.**

Although this database should be for production, let’s stick to what’s
eligible for the “Free Tier” and **go with the Dev/Test DB instance**. The
differences between the two are mainly in the realm of scalability and
performance.

On the next screen, do yourself a favor and click the checkbox with the label
`Only show options that are eligible for RDS Free Tier` next to it. The
resulting default settings are perfectly fine.

**If you haven’t been paying attention up to this point, now’s the time to
wake up.**

The `DB Instance Identifier` field will contribute to what will be the final
host name of the database. While it’s required, it’s not something that you’ll
need to keep a record of yourself.

You will however need a record of the `Master Username` and `Master Password`.
**These can/will be different from the username/password that you use to log
in to AWS.** These will serve as the username and password that you use to
access the database from whatever app you’re deploying. **Know what they
are.**

The default settings on the next screen are mostly fine. There are a few that
are important to modify:

  * `VPC Security Group(s)`: this database may be accessible by one or more applications. Therefore, you get the choice of using one (or more) of your existing security groups or of making a new one. **Whatever security group(s) is attached to this RDS instance will need a new Custom TCP rule for allowing Inbound access on Postgres’s post 5432.**
  * ` Database Name`: the actual name of the database going into your settings file. **Know what this is**.

Make sure that no matter what you choose for your `VPC Security Group`, the
**Public Accessibility** is set to “Yes”. **IF YOU DO NOT DO THIS, YOU WILL
NOT BE ABLE TO ACCESS YOUR DATABASE.** If you forget, you can always go back
later and change it.

Finally, click on the button for launching your instance. This will take
significantly longer than launching an EC2 instance (though stiill just short
enough for a class demo!).

Once your RDS instance is up and running, more more key piece of information
will become available to you: the `Endpoint`. This URL (minus the port number)
will serve as our `Host` URL.

Congratulations, you’ve now set up a remote database!

## Prepare `settings.py` for Deployment

Setting up the database is one thing. However, we’ve got an app that needs to
USE that database.

In our Django Lender’s `settings.py` file, there’s a few keywords there that
need to be modified (and a few that need to be declared) for the sake of
deployment.

  * [SECRET_KEY](https://docs.djangoproject.com/en/2.0/ref/settings/#secret-key)
  * DEBUG (should be set to `False` in production, `True` in development)
  * [ALLOWED_HOSTS](https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts)
  * [DATABASES](https://docs.djangoproject.com/en/2.0/ref/settings/#databases) and related information
  * [STATIC_ROOT](https://docs.djangoproject.com/en/2.0/ref/settings/#static-root)
  * [EMAIL_BACKEND](https://docs.djangoproject.com/en/2.0/topics/email/#smtp-backend) and related information. If our app is to be in production, it must send actual registration emails, and not just print them to the console anymore.

You could hard-code all of these values if you wanted, however there are
massive security issues that would result. You’d also have trouble running
your code locally, because all your settings would be attuned to what’s in
production.

There are a couple of ways of dealing with this.

One of the most commonly-cited methods (e.g. in [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11)) is
to convert your `settings.py` file into a `settings/` directory. You would
then fill that directory with a base settings file, and other files that
import those settings and override the necessary ones for production,
development, testing, etc.

There are a number of problems and lingering security issues with this method.
Not least of these problems is that you start to produce large divisions
between your app in development and in production. To have an adequate idea of
how your app will be run in production, **you need to have your development
settings be as close to your production settings as possible**. So, this
method won’t do.

The second method, championed by followers of the [12-Factor App](https://12factor.net/) is to have **one and only one settings file.**
Within that settings file, you import your configuration using environment
variables. Much like how we used the ` DATABASE_URL` environment variable to
set the `sqlalchemy.url` in the settings dict when we used Pyramid. Remember,
`os.environ.get()` allows you to set a default if the environment variable of
choice doesn’t exist, while `os.environ["KEY_NAME"]` will throw a `KeyError`
if the chosen variable doesn’t exist.

Remember the Master User, Database Name, Master Password, and Endpoint from
the RDS dashboard? Use those here.

## Prepare EC2 Instance to pull and start app

Finally you must get all of the files from your app onto the instance. You
could always `scp` everything over like we did for the simple WSGI app, but
that’s not a good or sustainable method. For one, you’re pushing development
code to your production machine. You should be able to use version control to
get the last stable copy of your software. You should be able to use `git`.

On your EC2 instance,

  * `sudo apt-get install git python3 python3.4-pip python3-venv`
  * add environment variables to the app environment

Finish hooking your deployed Django app all together with environment
variables tonight for homework. Remember, when `DEBUG=False`, your app will
behave somewhat differently than it did in development (e.g. static and media
files). Be aware!

