import pandas as pd

df = pd.read_csv("employees.csv")

print(df["Name"])

print(df[["Name", "Salary"]])

print(df.iloc[0])

print(df.loc[2])