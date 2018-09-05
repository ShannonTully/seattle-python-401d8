# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 18: Pyramid - Model Relationships

## Pyramid: Assign Stocks to Users

**This is a solo assignment**

We're adding relationships between Stocks and the Users that own them.

### Specifications

- In your `pyramid-stocks` repository create a branch called `class-18-relationships`
- Modify your `Stock` and `User` models to create a many-to-many relationship between them, where one `User` can have many `Stock`s, and every `Stock` can have many `User`s.
    + You will need to destroy and rebuild your database for this application to continue working
- Modify your views in the following ways:
    + Whenever a `Stock` is added to a user's portfolio:
        - it is added as a record in the stocks table, if it does not already exist
        - it gains the current authenticated `User` as one of its users if that user isn't already in that set
        - the authenticated `User` gains that stock as one of its own stocks if they don't already have it
    + An 'association table' will need to be generated and both your Stock and Account model will need to be used to populate the junction (association) table.
    + When a user's stocks are requested in the portfolio view, that user should only see the stocks related to their account and portfolio
    + When a user requests to view details about a given company, ensure that they are only able to view stock details for those that they have added to their portfolio.
        - _Note: this does not limit a user from searching for and viewing the details of a new stock that has not been added to their portfolio_


### Testing
- Ensure that both your views and models have been thoroughly unit tested. You should have at least three tests for each view controller, as well as each model. Your coverage reports should guide you to line coverage, and your goal is 80% or better in your coverage reports.


### Submission

1. Create a pull request from your `class-18-relationships` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-18-relationships` into `master`

---

## Project Prep: Write User Stories
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
