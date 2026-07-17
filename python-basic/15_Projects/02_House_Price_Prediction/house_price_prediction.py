import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("house_data.csv")

# Features and Target
X = data[["Area"]]
y = data["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction
area = 2700
predicted_price = model.predict([[area]])

print(f"Predicted Price for {area} sq.ft house: ${predicted_price[0]:.2f}")

# Visualization
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")

plt.title("House Price Prediction")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price ($)")
plt.legend()

plt.show()