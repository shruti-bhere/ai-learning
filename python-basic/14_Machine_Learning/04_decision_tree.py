from sklearn.tree import DecisionTreeClassifier

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()

model.fit(X, y)

print(model.predict([X[5]]))