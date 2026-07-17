import pandas as pd

employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Shruti", "Rahul", "Priya"]
})

salary = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [60000, 55000, 70000]
})

merged = pd.merge(employees, salary, on="ID")

print(merged)