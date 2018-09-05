# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 43: ReactJS Client for Django Imager

## ReactJS - Build a ReactJS client for your Imager app!

**This is a Pair assignment**

### Specifications

- Create a new repository calls `imager-react`
- Work in a branch called `react-client`
- Install your React scaffold using `npx install create-react-app imager`, and cd into that directory
- *BEFORE WORKING ON REACT*:
    - ensure that you've updated your Django application to provide RESTful interfaces for both user signup and signin, and optionally any other endpoints that you would like exposed for your React Client.
- Follow the below specification for building a React Imager Application:

Create the following components and structure them according to the following diagram
```
App
    BrowserRouter
        Navbar
        Landing
            AuthForm
            Library
```
###### App Component
* should contain all of the **application state**
* should contain methods for modifying the application state
* the state should have a topics array for holding the results of the search

###### Navbar Component
* should be present on all rendered component views across the site
* should have link components which represent and provide navigational routing to all defined client-side routes on the page
* (optional) should take user state from the App component, and conditionally render data about the User/Profile

###### Landing Component
* should conditionally render the AuthForm component with props that are determined by the path of the page (i.e. /signin or /signup)

###### AuthForm Component
*  should provide a single point form for both signup and signin
    - ensure that form field(s) not required for signin are not shown
* when form data is captured by submission, pass your frm data back to the application component for use in an API call to your backend


### Testing
- No testing.

### Submission

1. Create a pull request from your branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge your branch into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
