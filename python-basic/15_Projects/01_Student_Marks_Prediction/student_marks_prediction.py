import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("student_marks.csv")

X = data[["Hours"]]
y = data["Marks"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[9]])

print(f"Predicted Marks for 9 hours: {prediction[0]:.2f}")

# Plot
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction")
plt.show()