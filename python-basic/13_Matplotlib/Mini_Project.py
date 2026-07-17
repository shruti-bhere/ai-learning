"""
Employee Salary Dashboard
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["Salary"])

plt.title("Employee Salary")

plt.xlabel("Employee")

plt.ylabel("Salary")

plt.grid(True)

plt.show()