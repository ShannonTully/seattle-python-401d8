# Deploying Pyramid to Heroku
In which we learn how to make a simple Pyramid application run in the Heroku environment.

# Heroku’s Environment
Heroku is a great system for getting web applicatons up and running fast. But to work with it, you have to make sure that your application meets with Heroku’s expectations. Let’s take a moment to walk through setting up a simple Pyramid application to run on Heroku.

## Assumptions
This quick tutorial assumes that you have:

1. Created an account with Heroku
1. Installed the Heroku Toolbelt
1. Authenticated the toolbelt via heroku login or similar
1. Have created a Pyramid application that you want deployed

### Heroku Build Needs
The application deployment story for Heroku is tightly coupled to Git. It is not tightly coupled to GitHub. We’ll use GitHub here because it is familiar. But the same process will work for GitLab, BitBucket, or whatever.

Start by navigating to your repository root. The same place where your .git directory is located. As an example I’ll use the learning_journal app we’ve been constructing in class.
```sh
(ENV)$ pwd
/absolute/path/to/learning_journal
(ENV)learning_journal$
```
Now that we are at the root of our repository, we are ready to integrate Heroku.

### Tell Heroku This is Python
Heroku uses a series of heuristics to determine what type of application you have. The primary heuristic for a Python app is the presence of a requirements.txt (note: NOT requirements.pip) file at the same level as your `.git` directory*. It **MUST** be there or else Heroku will throw a fit, guaranteed.

Let’s create that file and add it to our repository:
```sh
(ENV)learning_journal$ pip freeze > requirements.txt
```
The file that was created will contain a reference to the learning_journal. However, you don’t actually want to install this with pip when on heroku. So edit the requirements.txt file to remove these lines:
```sh
## !! Could not determine repository location
learning_journal==0.0
```
Add that file to your git repository and commit:
```sh
(ENV)learning_journal$ git add requirements.txt
(ENV)learning_journal$ git commit -m "adds requirements file so Heroku knows it is a Python app"
```

### Tell Heroku You Want Python 3.6
As noted in this handy document on Heroku’s Python runtimes, Heroku supports Python 2.7.13 and 3.6.1, but defaults to Python 2.

But we want all of the Python 3.6 goodness we can handle!

Create a document at your repository root named runtime.txt. Within it, write this one line: `python-3.6.1`
```sh
(ENV)learning_journal$ echo "python-3.6.4" > runtime.txt
```
Add this file to your git repository and commit. Now your deployment will be in glorious Python 3.6.
```sh
(ENV)learning_journal$ git add runtime.txt
(ENV)learning_journal$ git commit -m "adds runtime file so Heroku runs in Python 3.6"
```

### Tell Heroku How to Run Your App
Heroku requires a plain text file called Procfile (spelling and capitalization count). This file tells Heroku what to do to run your application. Add this file to your repository, again at the repository’s root. It should contain the text web: `./run`
```sh
(ENV)learning_journal$ echo "web: ./run" > Procfile
(ENV)learning_journal$ git add Procfile
(ENV)learning_journal$ git commit -m "Tells Heroku how to run my app"
```
Because we wrote that line in Procfile, Heroku is going to look for an executable script by the name run in our application’s root directory. We need to make that file. We’d like it to install our application and then start up a server to serve it.

Create the file run in the repository root. Then type the following text into it:
```sh
#!/bin/bash
set -e

python setup.py develop
python runapp.py
```
This script tells the Heroku server to use the bash shell (`#!/bin/bash`). It says that if any part of the script returns an error, it should exit the script (`set -e`). Following that, Heroku installs our application in develop mode (equivalent to running pip install -e . when in the project root). Finally, it executes a Python module called `runapp.py`, which we have to create.

The run file needs to be executable, so that Heroku can run it. We can use the chmod shell command to fix that:
```sh
(ENV)learning_journal$ chmod u+x run
```
We’ve now made the file executable (that’s what the +x means). Add the file to your repository and commit it:
```sh
(ENV)learning_journal$ git add run
(ENV)learning_journal$ git commit -m "adds a shell script to start my app"
```

### Create the runapp.py module
Everything that we’ve written thus far is just so that Heroku can recognize our application and start up a worker to serve it. We still need to actually write the Python module that will run our application.

Create a file `runapp.py` in the project root and type the following Python code into it:
```python
import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:production.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)
```
In line 6, we use an if `__name__ == '__main__'` block to make this module a Python script that can run from the command line. The code in this block will only be executed when the script is run.

In line 7, we read the “PORT” variable from the operating system environment. Heroku uses environmental variables to pass information to applications. This allows you to separate configuration from code and is a good pattern. Notice that we default to port 5000 if no ‘PORT’ has been set in the environment.

In line 8, we create an application, using the production.ini file that is located adjacent to this Python module.

Finally, in line 10, we serve our application, setting it up to listen on any available IP address.

Add this file to our git repository and commit your changes:
```sh
(ENV)learning_journal$ git add runapp.py
(ENV)learning_journal$ git commit -m "adds a python script to run our application"
```

### Set Up Heroku and Deploy
Okay, with that, we’ve got all we need to get our app running on Heroku. Next, we’ll use the Heroku toolbelt to create a new app:
```sh
(ENV)learning_journal$ $ heroku create
Creating app... done, ⬢ safe-scrubland-24595
https://safe-scrubland-24595.herokuapp.com/ | https://git.heroku.com/safe-scrubland-24595.git
```
Finally, we push our app to heroku:
```sh
(ENV)learning_journal$ git push heroku master
...remote: Verifying deploy... done.
```
And once that is finished, you can view your app in a browser:
```sh
(ENV)learning_journal$ heroku open
```
If anything breaks during or after deployment, check the logs.
```sh
(ENV)learning_journal$ heroku logs
```
If you’re working on a branch of your repository and don’t want to merge the changes back to master yet before deploying those changes to Heroku, you can push that branch instead of master.
```sh
(ENV)learning_journal$ git push heroku <branchname>:master
```

### Cleaning Up the Edges
There’s one last problem here. Heroku defaults to serving our application over https. This is desireable.

But our Pyramid application has no idea that it is being served securely. When it generates the URLs for CSS files, it uses http. Our browsers will not appreciate this.

We can fix it using configuration.

Open the file production.ini from your application root directory in your text editor. First, find the first section header at the top that contains this [app:main]. Change that to read [app:learning_journal]

Next, find the section of the file that looks like this:
```ini
###
# wsgi server configuration
###

[server:learning_journal]
use = egg:waitress#main
host = 0.0.0.0
port = 6543
```
Before this section, add the following configuration:
```ini
[filter:paste_prefix]
use = egg:PasteDeploy#prefix

[pipeline:main]
pipeline =
    paste_prefix
    learning_journal
```

Lines 1-2 create a wsgi middleware filter that will detect the https scheme and make that information available to our Pyramid app.

Lines 4-7 set up a wsgi pipeline which puts this filter before our new app (remember, we changed the app name above to learning_journal).

Save these changes, add them to the stage, and commit them to your repository. Then you can re-deploy your application using git push:
```sh
(ENV)learning_journal$ git add production.ini
(ENV)learning_journal$ git commit -m "enables pyramid to properly render https urls for static resources"
(ENV)learning_journal$ git push heroku master
```
And that finishes us up. We now have a small, functional Pyramid application running on Heroku, serving resources over https. Later, you’ll repeat this process with your own learning journal application

### Only Once You Start Using Postgres
Congratulations, you’ve got a database running locally! Isn’t data persistence awesome? However, all of your data is only being persisted locally, which does nothing for the website you have on Heroku. When it’s deployed using production.ini, it’ll be pointing at the wrong database.

We could modify production.ini to set up a sqlalchemy.url for a Postgres database on our production server. However, this only works on a static server whose location we know. Heroku uses its own server to host its Postgres database, whose location we do not know. Further, they may copy the database and move it elsewhere without our knowledge. We want our data to persist no matter where it goes.

What we need is an Environment Variable. This is something that will belong to whatever environment we launch our site in. When you use the postgres add-on in Heroku, an environment variable becomes available to you called `DATABASE_URL`. `DATABASE_URL` holds the url for your Postgres database, and will be accessible no matter what Heroku does with it.

We need to make our Pyramid app look for that variable no matter what machine it’s on and always point to the proper database.

### Making and Seeing Environment Variables
Environment variables live in your environment’s bin/activate file, as well as in your shell config files.

You’ve already seen a few. For example, your `PATH`.
```sh
(ENV) bash-3.2$ echo $PATH
/Users/User/Documents/codefellows/courses/code401_python/pyramid_lj/bin:/Library/Frameworks/Python.framework/Versions/3.5/bin:/Users/User/:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/git/bin:/usr/texbin:/usr/local/bin:/Users/User/bin:/Applications/MAMP/Library/bin/:/Applications/mongodb/bin/:/Applications/Postgres.app/Contents/Versions/latest/bin
```
Your `PATH` variable holds all the places that your computer will look for console commands and Python packages. You can inspect it and any other environment variable using echo in the console.

Every environment variable gets prefixed by `$` when used in the shell. To see what’s currently available, type `ENV`.
```sh
(ENV) bash-3.2$ ENV
TERM_PROGRAM=Apple_Terminal
TERM=xterm-256color
SHELL=/bin/bash
...
... a bunch of variables and their values
```
You can create a new environment variable using the export command. You define that variable with some name and attach it to some value, like a string.
```sh
(ENV) bash-3.2$ export FOO="BAR"
(ENV) bash-3.2$ echo $FOO
BAR
```
Defining an environment variable in this way will not persist that variable across different terminal instances. To create a lasting variable, you have to add it to your .bashrc, .bash_profile, or the activate script in your virtual environment.
```sh
# pretty much anywhere inside ENV/bin/activate
...
export FOO="BAR"
...
```
Navigate back to the command line:
```sh
(ENV) bash-3.2$ deactivate

bash-3.2$ echo $FOO

bash-3.2$ source ENV/bin/activate
(ENV) bash-3.2$ echo $FOO
BAR
```
Note, if you add a variable to environment’s activate script, it’ll only be accessible in that environment. This is good. We want to be able to use this to isolate configuration for an app only to the environment in which the app lives.

### Calling Environment Variables
It’s actually fairly simple to call environment variables into Python. os.environ returns a dict-like object whose keys are the currently-available variables. Pop open a pshell and investigate.
```python
In [1]: import os
In [2]: for key, value in os.environ.items():
    print(key + " = " + value)
   ...:
   # ... a bunch of other variables
   # ...
   FOO = BAR
   # ...
   # ... even more variables

In [3]: os.environ["FOO"]
Out[3]: 'BAR'
```
If we defined our `DATABASE_URL` variable in `ENV/bin/activate`, then we could call that out too.
```python
In [4]: os.environ["DATABASE_URL"]
Out[4]: 'postgres://User@localhost:5432/learning_journal'
```
Similar functionality can be obtained from the `os.getenv()` function. For this, you must know exactly the name of the variable you’re looking for. That variable will be returned as a string.
```pythonn
In [5]: os.getenv("DATABASE_URL")
Out[5]: 'postgres://User@localhost:5432/learning_journal'
```

### Environment Variables in Pyramid
What we ultimately want to do is dynamically set the `sqlalchemy.url` to the value of our `DATABASE_URL` environment variable.

`learning_journal/__init__.py` is where our .ini file’s configuration gets bound to our Pyramid app. Before the current settings get added to the Configurator, we can use os.environ to bring in our environment’s `DATABASE_URL`. settings is, after all, a dictionary like any other.
```python
# __init__.py

import os

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    if os.environ.get('DATABASE_URL', ''):
        settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]

    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
```
Because we should always try to keep code DRY (and prevent future confusion), remove the `sqlalchemy.url` keyword from `development.ini` and `production.ini`.

If we invoke `pserve development.ini` and navigate to the site in the browser, everything should show up the same.

We just have to add one more line of code to make deployment smooth. Recall that in order to view the data in your database you have to run that initializedb shell command. We need to do something similar to set up the tables in our deployws application.

Why do it manually when you already have a script that’s automatically changing directories, installing your package, and running your app upon deployment? Let’s just migrate our pre-existing development database up to the app so we can play!
```sh
(ENV)learning_journal$ heroku pg:push entries_dev DATABASE_URL --app lj-demo
                     # heroku <postgres:push> <DB_NAME> <DB_URL> --app <APP_NAME>
```
