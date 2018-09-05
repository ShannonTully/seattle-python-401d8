# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 13: Pyramid - A Python Web Framework

## Pyramid: Start the Stock App

**This is a solo assignment**

This will be the first day of several dedicated toward building out a stock performance application.

The overall goal will be to allow users to log in, log out, add stocks to their portfolio so that they may monitor them, and eventually include a machine learning component that'll extract trends in their price history.

### Specifications

- Create a new repository called `pyramid-stocks` with a good Python `.gitignore` and MIT `LICENSE`
- In your `pyramid-stocks` repository create a branch called `class-13-pyramid-views`
- On this branch, create your Pyramid scaffold using the `cookiecutter` template for a SQLAlchemy scaffold.
- Convert the templates that you built in the `templates` directory into Jinja2 templates in your application's `templates` directory
- Ensure that your application can accept requests to the following routes, and render the appropriate template:
    + `GET /` - the home route
    + `GET /auth` -  for registering a new account and signing up; should not be functional, and you don't need to worry about distinguishing between the two yet.
    + `GET /stock` - for searching for a stock ticker symbol; should not be functional
    + `GET /portfolio` - for a user's existing stocks; should not be functional
    + `GET /portfolio/{symbol}` - for detail about a user's existing stock, where `{symbol}` is variable; should not be functional, and you likely won't be able to get to this route given that you have no data to work with today.

- Ensure that each of the above routes displays the appropriate template


### Submission

1. Create a pull request from your `class-13-pyramid-views` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-13-pyramid-views` into `master`

---

## Project Prep: Create a Repository
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
