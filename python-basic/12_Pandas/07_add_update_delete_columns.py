import pandas as pd

df = pd.read_csv("employees.csv")

df["Bonus"] = df["Salary"] * 0.10

df["Age"] = df["Age"] + 1

df.drop("Age", axis=1, inplace=True)

print(df)