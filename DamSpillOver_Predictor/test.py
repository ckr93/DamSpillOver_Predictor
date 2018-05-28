import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV

from sklearn import metrics
from pandas._libs.parsers import na_values
from pandas.tests.io.parser import skiprows
from sklearn import neighbors, preprocessing, cross_validation

dataset = pd.read_csv('E:/FYP Project/DamSpillOver_Predictor/predictor/dataset/FinalFormattedData.csv', na_values="?")

dataset.dropna(inplace=True, axis=0, how="any")

dataset.apply(pd.to_numeric)

X = dataset.loc[:,"Year":"Rainfall"]

y = dataset["Elevation"]

print('print X_test', X)
print('print X_test', y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# print('print X_test', X_test)
# print('print', X_train)

clf = neighbors.KNeighborsClassifier(30)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
y_pred = clf.predict(X_test)
print("printing chances: ", y_pred[:10])
print("acuracy score is ", accuracy_score(y_test, predictions))
prediction=clf.predict([[2017,11,25,468.44,64.88,2.02,0.81,0,0,1.84,5.5]])

print('prediction is ', prediction)

# print(metrics.classification_report(y_test, y_pred))
#
# metrics.precision_recall_curve(y_test, y_pred)
