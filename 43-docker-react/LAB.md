# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 43: ReactJS Intro

## ReactJS - Introduction to Components and State Management

**This is a Solo assignment**

### Specifications

- Create a new repository calls `reddit-search`
- Work in a branch called `react-intro`
- Install your React scaffold using `npx install create-react-app <name of the app>`, and cd into that directory
- Follow the below specification for building a Reddit Search Application:

Create the following components and structure them according to the following diagram
```
App
  SearchForm
  SearchResultList
```
###### App Component
* should contain all of the **application state**
* should contain methods for modifying the application state
* the state should have a topics array for holding the results of the search

###### SearchForm Component
* should contain a text input for the user to supply a reddit board to look up
* should contain a number input for the user to limit the number of results to return
  * the number must be more than 0 and less than 100
  * `onSubmit` the form should make a request to reddit
  * it should make a get request to `http://www.reddit.com/r/${searchFormBoard}.json?limit=${searchFormLimit}`
    - _Note: `www` is **required** for the api call to complete successfully._
  * on success it should pass the results to the application state
  * on failure it should add a class to the form called error and turn the form's inputs borders red

###### SearchResultList Component
* Should inherit all search results through props
* This component does not need to have its own state
* If there are topics in the application state it should display an unordered list
* Each list item in the unordered list should contain the following
  * an anchor tag with a href to the topic.url
    * inside the anchor a heading tag with the topic.title
    * inside the anchor a p tag with the number of topic.ups


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
