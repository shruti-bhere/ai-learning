from sklearn.neighbors import KNeighborsClassifier

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

print(model.predict([X[0]]))