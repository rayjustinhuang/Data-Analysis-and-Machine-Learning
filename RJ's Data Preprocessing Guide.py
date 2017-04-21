# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 18:12:28 2017

@author: Justin
"""

# Data Preprocessing

# Import libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Read in dataset
df = pd.read_csv('Data.csv')

# View summary and info
df.head()
df.info()

# Create X (dependent) and y (independent) matrices
X = df.drop('Purchased', axis = 1)
y = df[['Purchased']]

# Impute missing values
from sklearn.preprocessing import Imputer
X_imputer = Imputer(missing_values = 'NaN', strategy = 'mean')
X[['Age', 'Salary']] = X_imputer.fit_transform(X[['Age', 'Salary']])

# Import encoding classes
# NOTE: I personally prefer using pandas get_dummies versus these sklearn
# classes, which (in my opinion) require a lot more work for similar results
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Encoding strings
labelencode = LabelEncoder()
X['Country'] = labelencode.fit_transform(X['Country'])

# Dummy coding
dummycode = OneHotEncoder()
X[['France', 'Germany']] = pd.DataFrame(dummycode \
 .fit_transform(X[['Country']]).toarray()).iloc[:, :-1]
X.drop('Country', inplace=True, axis = 1)

# [Optional] Reorder columns
X = X[['France','Germany', 'Age', 'Salary']]

# Split into training and test sets
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
                                                    random_state = 47)

# Important note: train_test_split returns VIEWS of the split DataFrame, 
# NOT COPIES. As such, to apply transformations such as scaling without
# warnings, I create copies of the X_train and X_test DataFrames in the 
# next few lines of code.

# Scale features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Here are the copies I was talking about
scaled_X_train = X_train.copy()
scaled_X_test = X_test.copy()

scaled_X_train[['Age', 'Salary']] = scaler \
.fit_transform(X_train[['Age', 'Salary']])
scaled_X_test[['Age', 'Salary']] = scaler.transform(X_test[['Age','Salary']])

# Perform basic data viz
# NOTE: This is usually done after imputation but prior to feature scaling
# NOTE: The samples below are hardly complete; be creative and do what suits
# the data you're analyzing

# Pandas built-in
df.hist()
X.plot()

# Matplotlib
# NOTE: It is ideal to use the object-oriented method of generating plots.
# Create figures first using: fig = plt.figure() AND ax = fig.add_axes()
# OR fig, ax = plt.subplots(). Pass in arguments as necessary
plt.hist(X['Age'])
plt.scatter('Age', 'Salary', data = X)

# Seaborn
sns.jointplot('Age','Salary', data = X, kind='reg')
sns.distplot(X['Age'])
