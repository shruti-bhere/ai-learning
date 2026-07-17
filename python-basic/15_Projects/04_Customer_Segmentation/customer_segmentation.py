import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Dataset
data = pd.read_csv("customer_data.csv")

# Features
X = data[["AnnualIncome", "SpendingScore"]]

# KMeans Model
model = KMeans(n_clusters=3, random_state=42)

# Train Model
model.fit(X)

# Cluster Prediction
data["Cluster"] = model.labels_

print(data)

# Cluster Centers
print("\nCluster Centers")
print(model.cluster_centers_)

# Visualization
plt.figure(figsize=(8,6))

plt.scatter(
    data["AnnualIncome"],
    data["SpendingScore"],
    c=data["Cluster"],
    cmap="viridis",
    s=100
)

plt.scatter(
    model.cluster_centers_[:,0],
    model.cluster_centers_[:,1],
    color="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()

plt.show()