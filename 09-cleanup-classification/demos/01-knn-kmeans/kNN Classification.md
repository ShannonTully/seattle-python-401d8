
# SUPERVISED CLASSIFICATION - kNN ALGORITHM

### GOAL: Show supervised classification on the example of kNN algorithm


```python
# Import the necessary modules

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
```


```python
# Set the number of nearest neighbors to consider ("k" in kNN)

n_neighbors = 15

# Import the Iris dataset. It is conveniently embedded in sklearn. Neat!
iris = datasets.load_iris()

# Take the first two features
X = iris.data[:, :2]
y = iris.target
```


```python
# We will classify every point in space

h = .02  # step size in the mesh

```


```python
# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

```


```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
```


```python
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
```


```python
for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_train, y_train)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    print("xx shape: {0}".format(xx.shape))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cmap_bold, edgecolor='k', s=20)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.title("3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.show()
```

```python
pred = clf.predict(X_test)

```


```python
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, pred))
```

```python
print(classification_report(y_test, pred))
```

# What is Precision and Recall?

![TP, TN, FP, FN image](Precisionrecall.png)

# What is f1 score?

## f1 = 2 x Precision x Recall / (Precision + Recall)

# What is support?

## Simply the number of samples of that class in y_test

## In fact, there is a continuum between supervised and unsupervised classification. When only part of the data is labeled - we use semi-supervised classification.
## One idea: to cluster unlabeled data and assign to points  in each cl
