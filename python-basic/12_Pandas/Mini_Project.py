"""
Employee Salary Analysis
"""

import pandas as pd

df = pd.read_csv("employees.csv")

print("Employee Details")
print(df)

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nHighest Salary")
print(df["Salary"].max())

print("\nLowest Salary")
print(df["Salary"].min())

print("\nEmployees in AI Department")
print(df[df["Department"] == "AI"])

print("\nDepartment-wise Average Salary")
print(df.groupby("Department")["Salary"].mean())