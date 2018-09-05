# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 08: Regressions

## Model a relation in a dataset using a regression

**This is a solo assignment**

You will do some exploratory analysis of a dataset, finding likely candidates.

### Specifications

The "Ecommerce Customers" dataset represents data from a fictious store with fictious customers. Customers come in the store to get style advice, and them come home and order clothes either via the company's website or the mobile app. The dataset describes for each customer the yearly amount spent, as well as the duration of average advice session, time spent on the app and on the website, and length of store membership. You will have to answer a question, whether the company should concentrate further efforts on improving the website or the mobile app.

- In your `data-science` repository, create a branch called `class-08-regression`
- Copy the [Ecommerce Customers](./assets/ecommerce-customers) dataset into the repository
- Start a Jupyter Notebooks called `regression`
- Add a markdown cell at the top of each notebook with the title of this assignment, the name of the data set, as well as your name and the date
- Load up this data set into a Pandas DataFrame
- In the `regression` notebook answer the following questions/do the following tasks
  1. Show the first 5 rows of the dataset
  1. Show the `description` and the `info` on the dataset, using appropriate Pandas functions
  1. Use seaborn `jointplot` function to see which fields correlate well with the "Yearly Amount Spent" column. Write your findings.
  1. Make a summary plot of feature relationships using `pairplot` function of Seaborn
  1. Create two dataframes: one for the target variable ("Yearly Amount Spent"), the other - containing all the rest of numerical features
	1. Split the data into a training and test sets. Make a test set size `0.3` and random seed `123` (so the results are consistent for all students)
	1. Fit a regression model on the training set
	1. Print out the coefficients of the model
	1. Make a prediction of the target variable from features dataframe
	1. Calculate the Mean Squared Error (using `sklearn.metrics` module)
	1. Using Seaborn `distplot` show the histogram of the residuals - differences between the target variable and predicted target variable
	1. Answer the main question: How should we allocate the engineering budget between website development and app development?
	    - _Hint: look at the regression coefficients and contemplate their meaning_

### Submission

1. Create a pull request from your `class-08-regression` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-08-regression` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
