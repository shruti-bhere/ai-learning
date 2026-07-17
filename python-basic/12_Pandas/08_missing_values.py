import pandas as pd

data = {
    "Name": ["Shruti", "Rahul", None],
    "Salary": [60000, None, 50000]
}

df = pd.DataFrame(data)

print(df.isnull())

print(df.fillna(0))