import pandas as pd
from Optimization import Optimization

# Importing the dataset
dataset = pd.read_csv('data.csv')

# Check for NULL values
dataset.info()
dataset.isnull().sum()

# Give non-seizure patients zero values (avoided for-loop - might check individual instances later)
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

import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer (Represents 1 row)
classifier.add(Dense(output_dim = 85, init = 'uniform', activation = 'relu', input_dim = 177))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 35, init = 'uniform', activation = 'relu'))

# Adding the output layer
# If more than 1 independent vars - dim = # of vars, activation = softmax
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
# If dep var has more than 2 outcomes, loss = categorycall_crossentropy?
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
# Batch size - # of rows before updating weights
# nb_epoch - training occurs over a specified # of epoch's 
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
