# ![cf](http://i.imgur.com/7v5ASc8.png) Class 10: Stacks and Queues

## Implement a Stack and a Queue
**This is a solo assignment**

### Specification
- Create a new branch in your `data-structures-and-algorithms` repository called `stack-queue`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Create two separate directories: `stack` and `queue` respectively, with all of your standard module configuration for each directory
    - `__init__.py`, `README.md`, etc.

- Create two files _in each_ called `node.py` and `stack.py`, `queue.py` respectively
- In `node.py`:
    - Create a Class for a `Node` which is aware of the value as `val` and next as `_next`
        - Ensure that you have a `__repr__` method defined to return the value of the node when printed

- In `stack.py`:
    - Create a Class for a `Stack` which creates an empty Stack when instantiated
        - This class should be aware of a default `None` value assigned to `top` when the isntance is created
        - This class should be aware of the `len` of the stack, which represents the count of Nodes in the stack at any time
        - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the stack for each value in the iterable
        - Define any further magic methods such as `len` and `str` to support user functionality and informative responses
        - Define a method called `push` which takes any value as an argument and adds that value to the `top` of the stack with an O(1) Time performance
        - Define a method called `pop` which takes no arguments and removes / returns the Node at the top of the stack
        - Define a method called `peek` which takes no arguments and returns the Node at the top of the stack

- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.
- Every bit of functionality that you have should be tested and documented. As a general standard, you should have three tests for each method or body of functionality in your API.

- In `queue.py`:
    - Create a Class for a `Queue` which creates an empty Queue when instantiated
        - This class should be aware of a default `None` value assigned to `front` when the isntance is created
        - This class should be aware of a default `None` value assigned to `back` when the isntance is created
        - This class should be aware of the `len` of the queue, which represents the count of Nodes in the queue at any time
        - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the queue for each value in the iterable
        - Define any further magic methods such as `len` and `str` to support user functionality and informative responses
        - Define a method called `enqueue` which takes any value as an argument and adds that value to the `back` of the queue with an O(1) Time performance
        - Define a method called `dequeue` which takes no arguments and removes / returns the Node at the `front` of the queue

- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.
- Every bit of functionality that you have should be tested and documented. As a general standard, you should have three tests for each method or body of functionality in your API.


### Submission
1. Create a pull request from your `stack-queue` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `stack-queue` into `master`


----

## Build HTML Pages

**This is a solo assignment**

Mid-way through next week we'll be building an application that allows us to list and analyze data about stocks.
It'll be a web application, and it helps to have the HTML pages built for that ahead of time.

The overall goal will be to allow users to log in, log out, add stocks to their portfolio so that they may monitor them, and eventually include a machine learning component that'll extract trends in their price history.

### Specifications
- Create a new repository called `stock-portfolio` with a good Python `.gitignore` and MIT `LICENSE`
- In your `stock-portfolio` repository create a branch called `mockups`
- On your `templates` branch create a `mockups` directory
- In your `mockups` directory create 6 HTML files:
    + `index.html`: home page; flavor text introducing the application, along with buttons for logging in and registration
    + `register.html`: a form prompting the user to submit a new username, password, and password confirmation
    + `login.html`: a form prompting the user to submit a username and password combination
    + `stock-add.html`: a simple search bar that takes in ticker symbols in an input field. The button should say "Add to Portfolio"
    + `portfolio.html`: a listing of stock ticker symbols and their prices per share; it's fine to have it in the form of a table
    + `stock-detail.html`: a page that shows the detail of a stock. Consider [this](https://finance.yahoo.com/quote/MSFT?p=MSFT) for inspiration (minus all the news). At least show the price, the change, opening price, closing price, and volume
- Style your documents using SMACCS principles for organizing your stylistic content. You **may not** use a css framework like Bootstrap or Skeleton.


You **do not** need to include JavaScript/jQuery functionality in your scaffold, yet. These templates are meant to give you a practical wireframe-based approach to implementing your views as we progress through the next couple weeks. It should also give you a great head start on your stylistic planning and at least a partial implementation.


### Submission
1. There is no submission for this assignment. Please have it ready to work with by Weds.

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
