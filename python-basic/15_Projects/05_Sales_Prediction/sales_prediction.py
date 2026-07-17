import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("sales_data.csv")

# Features
X = data[["TV", "Radio", "Newspaper"]]

# Target
y = data["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("Actual Sales")
print(y_test.values)

print("\nPredicted Sales")
print(prediction)

# Accuracy
print("\nMean Absolute Error:", mean_absolute_error(y_test, prediction))
print("R2 Score:", r2_score(y_test, prediction))

# Predict new advertisement budget
new_data = [[150, 20, 30]]

new_prediction = model.predict(new_data)

print("\nPredicted Sales for TV=150, Radio=20, Newspaper=30")

print(new_prediction[0])