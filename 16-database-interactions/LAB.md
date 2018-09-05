# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 16: Pyramid - Models and Database Interaction

## Pyramid: The Stock Model

**This is a solo assignment**

We're continuing to build the stock portfolio application.
We'll be creating models that will be our data representations.

### Specifications

- In your `pyramid-stocks` repository create a branch called `class-16-pyramid-models`
- _Note: Do not delete your `sample_data` directory. We are going to continue to use it to seed our DB._
- In the `development.ini` and `production.ini`:
    + include the link to your postgres database; use a different database for each.
- In the `__init__.py` in your application root...
    + include your project's `models` directory into your site configuration
- In the `models` directory...
    + delete `mymodel.py`
    + create a file called `stock.py`
    + In `stock.py` create the `Stock` model with all of the same attributes that we've used in our sample data to this point. _Remember that you also need to define an `id` as your `primary key` as well._
    + create a file called `account.py`
    + In `account.py` create a `Account` model with the following attributes:
        * `id` - integer, autoincrementing; the ID number of the object in the database
        * `password` - string; the user's password
        * `email` - string; the user's email
        * `username` - string; the user's nickname
    + inside of `__init__.py` make sure you are no longer importing from `mymodel` and instead are importing Models from `stock.py` and `account.py`
- In `initializedb.py`...(seed the database with your mock data)
    + make sure you're not importing from `mymodel`, and are importing your models
    + within the `main()` function definition, ensure that you update the functionality to iterate through your sample data, and cast each item to a Stock instance
    ```python
        with transaction.manager:
            dbsession = get_tm_session(session_factory, transaction.manager)

            # NOTE: Made significant changes here
            from ..sample_data import MOCK_ENTRIES
            for entry in MOCK_ENTRIES:
                model = Entry(**entry)
                dbsession.add(model)
    ```
- In the `views` directory...
    + whenever a `GET` request is sent to your "search_stock" view...
        * use the requests library to gather the company information from your API, and present it to the client using your associated template.
        * if it can't be found, reload the form page with an appropriate error
        * if it can be found return that company info to the view, and render it out to the template
        * provide a mechanism (a button) to then trigger a `POST` request to the same route, and add the complete record to the stock table in your database.
    + whenever a `POST` request is sent to your "search_stock" view...
        * capture the `POST` request and associated stock model data in the same view definition, and store that complete `Stock` isntance in your database.
        * if it already exists in the database, update the record
        * on a successful `POST`, redirect to the `portfolio` page

<!-- - Your tests don't need to cover all of Pyramid's functionality, as you didn't write Pyramid yourself. Your tests only need to cover the view functions and models that you wrote. -->

### Submission

1. Create a pull request from your `class-16-pyramid-models` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-16-pyramid-models` into `master`

---

## Project Prep: Build Project Wireframes
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
