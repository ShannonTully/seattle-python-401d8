# Python Web Frameworks in the Wild
Source: [Python Web Frameworks](https://wiki.python.org/moin/WebFrameworks)

## Frameworks We Teach
We will be installing and using the following two web frameworks because without them, we’d have to do a lot of stuff ourselves that we may not want to do (or may not be able to do well). Frameworks give you a set of tools to deal with incoming requests, return responses to those requests, interact with a database, create programmable templates for creating web front-ends, etc.

### Pyramid
Pyramid makes it extremely easy to write web applications, whether small or large. Unlike larger frameworks, Pyramid makes fewer decisions for you and demands less of you. Unlike smaller frameworks such as Flask, Pyramid allows your app to grow when it needs to, without complicated refactoring. Pyramid focuses on producing a simple, finished product regardless of the size.

### Django
Django is unarguably the most popular Python Web framework. It encourages rapid development and clean design. Django has more moving parts than Pyramid, and a steeper learning curve. But the large ecosystem of add-ons that have been created (see django packages) means that Django is also more easily customized. You can use Django to make a full site if you want, or to encapsulate some smaller piece of functionality that you want to use across multiple projects.

### The Wider World of Python Frameworks
There are many other Python web frameworks, scores, in fact. If you’re interested in a survey, you can get this free pamphlet from O’Reilly to learn about the most downloaded of the current crop. Here are some other Python Frameworks and some notable sites built either entirely by or using parts of those frameworks.


## Installation
In order to begin working with Pyramid, we have to install it. We’ll also install the extension that allows Pyramid to interact with iPython, so that we get a nice-looking interpreter instead of the default Python one:
```
(ENV) $ pip install pyramid pyramid_ipython
```
The version that should be pulled down is the latest version, 1.8. Note the other packages that get installed along with it, as it has dependencies. For example, WebOb provides an HTTP Request and Response class, and those you work with in Pyramid inherit from them. Many other frameworks also use this package.

When it is installed, Pyramid creates a bunch of new shell commands (pcreate, pshell, prequest, etc). You can see them all in the bin directory of your virtual environment.
```
(ENV) $ ls ENV/bin
activate         hupper           pcreate          prequest         pviews
activate.csh     iptest           pdistreport      proutes          pygmentize
activate.fish    iptest3          pip              pserve           python
easy_install     ipython          pip3             pshell           python3
easy_install-3.6 ipython3         pip3.6           ptweens
```

### Writing a “Hello World” App
Source: trypyramid.com.
As is tradition, when using a new bit of technology we test that it works by having it print something like “Hello World”. This is no different. Make a directory for your “hello world” app called hello_world. Within that directory create a file named app.py and type the following:
```python
"""Simple Hello World! app."""
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    """Basic view for the hello_world application."""
    return Response("Hello World!")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
```
Save that file and run the following from the command line:
```
(ENV) $ python app.py
```
Notice how the shell returns nothing. This is a good thing. That means that the server you’ve set up through Pyramid is running and listening for requests.

Finally, open http://localhost:6543/ in your browser. This will simply connect you to the port that you told Pyramid to listen to, at 6543.

This is an almost irresponsibly-simple web application. It proves that the Pyramid framework can handle HTTP requests and generate HTTP responses. We’ll definitely be using Pyramid for significantly more-complex things. You can see that it is easy to get a simple site up and running with Pyramid. For the more complex stuff, it helps to have some structure set up beforehand.

