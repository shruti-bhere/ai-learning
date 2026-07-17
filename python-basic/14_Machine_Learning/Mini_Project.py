"""
Student Marks Prediction
"""

from sklearn.linear_model import LinearRegression
import numpy as np

hours = np.array([[1], [2], [3], [4], [5]])

marks = np.array([35, 50, 65, 80, 95])

model = LinearRegression()

model.fit(hours, marks)

prediction = model.predict([[6]])

print(f"Predicted Marks for 6 study hours: {prediction[0]:.2f}")