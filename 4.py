from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()
X = boston.data
y = boston.target

print(X)
print(X.shape)
print("Y")
print(y)
print(y.shape)

#algorithm
l_reg = linear_model.LinearRegression()

i = 0 #0-12
plt.plot(X.T[i],y)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5)

#training
model = l_reg.fit(X_train, y_train)
prd = model.predict(X_test)
print(f"Predictions {prd}")

print(f"Acc:  {l_reg.score(X,y)}")
