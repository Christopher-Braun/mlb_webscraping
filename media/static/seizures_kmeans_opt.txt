import matplotlib.pyplot as plt
import matplotlib.figure as figure
import numpy as np
import pandas as pd
import xgboost
from xgboost import XGBClassifier
from xgboost import plot_importance
from xgboost import plot_tree
from xgboost import to_graphviz
from Optimization_pca_cls import pca_optimization, cls_optimization


# Importing the dataset
dataset = pd.read_csv('data.csv')

# Check for NULL values
dataset.info()
dataset.isnull().sum()

# Give non-seizure patients zero values (avoided for loop - might check individual instances later)
dataset['y'] = dataset['y'].replace([5], [0]).ravel()
dataset['y'] = dataset['y'].replace([3], [0]).ravel()
dataset['y'] = dataset['y'].replace([4], [0]).ravel()
dataset['y'] = dataset['y'].replace([2], [0]).ravel()

X = dataset.iloc[:, 1:178].values
y = dataset.iloc[:, 179].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling (MUST BE APPLIED IN DIMENSIONALITY REDUCTION)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Applying PCA
# explained_variance - list of principle components and % of variance explained by each of them
# Run with n_components = None 1st (look at explained_variance)

pc_op = pca_optimization(X_train, X_test, y_train, y_test, d=3)

cl_op = cls_optimization(X_train, X_test, y_train, y_test, n_opt = int(pc_op[3])+1)

classifier = pc_op[6]
X_train = pc_op[4]

for i, j in enumerate(np.unique(y_set)):
    if j == 0:
        X1 = X_set[y_set == j, 0]
        X2 = X_set[y_set == j, 1]
    else:
        X3 = X_set[y_set == j, 0]
        X4 = X_set[y_set == j, 1]

plt.scatter(X1, X2, c = 'red')
plt.scatter(X3, X4, c = 'green')
plt.show()

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('KNeighbors (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('KNeighbors (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('KNeighbors (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()

f = plt.figure(figsize=(10, 8))
ax = plt.subplot(aspect='equal')
sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
                c=palette[colors.astype(np.int)]
                
                

    