# Testing Your Pyramid App
THIS WILL NOT BE COMPLETE, JUST AN EXAMPLE OF A COUPLE TESTS

Thus far we have written a bit of code for handling HTTP routing and serving data. But we haven’t yet written any tests of our own to make sure that things work the way that we need them to work. We can fortunately do this with Pyramid’s own testing module (Documentation).

When it comes to testing your Pyramid app (as well as other apps in general), you need to not only perform unit tests for individual pieces of functionality. You also need to test for how things perform when in practice. For example, if your app sends an email, you need to check that the email is actually sent.

However, for today, we’ll focus only on unit tests, refactoring and building out more about functional tests later.

### Setting Up a Test for a View
Our scaffold provided for us a tests.py file complete with some basic tests. However, since we won’t be using unittest for our test suite we’ll gut it completely. In its place, write:
```python
# in tests.py

from pyramid import testing
from pyramid.response import Response


def test_home_view_returns_response():
    """Home view returns a Response object."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert isinstance(response, Response)

def test_home_view_is_good():
    """Home view response has a status 200 OK."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert response.status_code == 200

def test_home_view_returns_proper_content():
    """Home view response has file content."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert "This is text in an external file" in response.text
```
As part of the setup, we have Pyramid’s own testing module. This module provides tools to set up the configuration we need for our app. It also gives access to the request and response objects that we need to test our views. Recall that our views must be called with a request as an argument. Depending on what work your views must do, this can be any Python object, even a simple string or dict. But if you require something with a bit more resemblance to a real request, you can use testing.DummyRequest.

Recall that our home_page view returns a Response object filled with some text. We make our tests reflect that. First we check that what was returned by our view callable is a Response object.
```python
# tests.py
from pyramid import testing
from pyramid.response import Response


def test_home_view_returns_response():
    """Home view returns a Response object."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert isinstance(response, Response)
```
Then we check that the request was processed properly, returning a status 200.
```python
def test_home_view_is_good():
    """Home view response has a status 200 OK."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert response.status_code == 200
```
Finally, we test that the actual content of the response matches what we expect.
```python
def test_home_view_returns_proper_content():
    """Home view response has file content."""
    from demo_app.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert "This is text in an external file" in response.text
```

## Running Pyramid Tests

To run these tests we have to first install all the packages that we need for testing. We defined those in our setup.py so just navigate to the project root and install like so:
```
(ENV) $ pip install -e .[testing]
```
We have .[testing] because we want to install everything in the current directory (the .), but we also want the extra packages that we specified for testing. If you have other extra packages you want for some other reason, you install them in this fashion.

Now that all is installed, run our tests!
```
(ENV) $ py.test demo_app -v
```
The -v flag makes your test output verbose, telling you the name of every test that passes/fails. For less verbose output, use -q.

