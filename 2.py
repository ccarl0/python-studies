import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("car.data")


X = data[[
    'buying',
    'maint',
    'safety'
]].values
y = data[['class']]

#converting data
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = Le.fit_transform((X[:, i]))


#convert y
label_maping = {
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}
y['class'] = y['class'].map(label_maping)
y = np.array(y)


#create model (knn)

knn = neighbors.KNeighborsClassifier(n_neighbors = 15, weights='uniform')
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
knn.fit(X_train,y_train)
prd = knn.predict(X_test)
acc = metrics.accuracy_score(y_test, prd)
print(f"prediction: {prd}")
print(f"acc: {acc}")

a = 21
print("actual value: ", y[a])
print("prediction: ", knn.predict(X)[a])
