from sklearn.cluster import KMeans

import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 9],
    [9, 10],
    [10, 11]
])

model = KMeans(n_clusters=2, random_state=42)

model.fit(X)

print(model.labels_)