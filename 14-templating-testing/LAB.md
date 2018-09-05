# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 14: Pyramid - Templating, Testing, and Flow Control

## Pyramid: Enhance the Templates

**This is a solo assignment**

This will be the first day of several dedicated to building out a stock performance application.

The overall goal will be to allow users to log in, log out, add stocks to their portfolio so that they may monitor them, and eventually include a machine learning component that'll extract trends in their price history.

### Specifications

- In your `pyramid-stocks` repository create a branch called `class-14-pyramid-templating`
- Create a `sample_data` directory inside of your application's root. Within this directory, create an `__init__.py` file that defines a variable called `MOCK_DATA`.
    + `MOCK_DATA` will be a list of at least 10 dictionaries.
    + Each dictionary within the above list will be of the format:
        ```python
        # You're welcome to use this as your first record!
        {
            "symbol": "GE",
            "companyName": "General Electric Company",
            "exchange": "New York Stock Exchange",
            "industry": "Industrial Products",
            "website": "http://www.ge.com",
            "description": "General Electric Co is a digital industrial company. It operates in various segments, including power and water, oil and gas, energy management, aviation, healthcare, transportation, appliances and lighting, and more.",
            "CEO": "John L. Flannery",
            "issueType": "cs",
            "sector": "Industrials"
        }
        ```
- Your Jinja2 templates should use template inheritance instead of repeating any of the site's layout
- Your template's links to the app itself, the navigation items, should be done using `request.route_url` instead of being hardcoded
- Your CSS, JavaScript, or image files that are stored in your `static` directory should be included with `request.static_url` instead of being hardcoded
- Your `/portfolio` route should use a `{% for %}` loop to populate the stock list using the data in `sample_data/__init__.py`
- Your `/portfolio/{symbol}` route should populate the data for the page based on the data from `sample_data/__init__.py`
- `/auth`, when submitted, should redirect the user to the portfolio page. No need to worry about distinguishing your forms on the page at this point. `POST /auth` for your signup and `GET /auth` for your signin, are sufficient.
    - You do not need to collect the form data or authenticate the user, yet, rather just ensure that you are able to receive the request on the server, and redirect the client to the portfolio page.

### Stretch Goal
- `GET /stock` - should use `requests` to find information online about the given ticker symbol and add it to the data in `MOCK_DATA`. These additions are in-memory, so you do not need to write them to the file directly; they will only persist while the app is live for any one session.
    - You will be using a free API from [IEX TRADING](https://iextrading.com/developer/docs), which does not require the use of an API key at this point.
    - We are specifically interested in the Company Info and the Time Series info, both of which are accessible via an API call using a companies Stock Symbol.

### Testing
- Your tests don't need to cover all of Pyramid's functionality, as you didn't write Pyramid yourself. Your tests only need to cover the view functions that you wrote.
- Write a series of tests which cover your view controllers and any other functionality that you've specifically defined within the scaffold. This should include only unit tests today.


### Submission

1. Create a pull request from your `class-14-pyramid-templating` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-14-pyramid-templating` into `master`

---

## Project Prep: Create a Readme
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
