# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 09: Classification

## Model a relation in a dataset using

**This is a solo assignment**

Classify data using the k-Nearest Neighbors algorithm, selecting an optimal `k`.

### Specifications

You will need to explore a dataset and run a kNN classifier on it. You are also required to find the optimal value on k - the number
of nearest neighbors for kNN classifier.

- Continue working in your `data-science` repository, and in that repository create a branch called `class-09-kNN`
- Copy the [KNN_Project_Data](./assets/knn-project-data) dataset into the repository
- Start a Jupyter Notebooks called `kNN`
- Add a markdown cell at the top of each notebook with the title of this assignment, the name of the data set, as well as your name and the date
- Load up this data set into a Pandas DataFrame
- In the `kNN` notebook answer the following questions/do the following tasks.
    1. Show the first 20 rows of the dataset
    1. Show the `description` and the `info` on the dataset, using appropriate Pandas functions
    1. Use seaborn `pairplot` function to see which pairs of features form nice clusters
    1. Split the data into training set and test set. Make a test set size 0.3 and random seed 123 (so the results are consistent for all students)
    1. Standartize the variables - scale them to zero mean and unit variance. Do not pass the "TARGET CLASS" column to the scaler!
	1. Check that the features are indeed scaled
	1. Fit the kNN to the training data. Use k = 1.
	1. Check the classifier performance
	1. Try different k values and select one that works best. The way to do it is to see when increasing k does not add to performance anymore.

### Submission

1. Create a pull request from your `class-09-knn` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-09-knn` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
