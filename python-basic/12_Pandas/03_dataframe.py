import pandas as pd

data = {
    "Name": ["Shruti", "Rahul", "Priya"],
    "Age": [22, 24, 23],
    "City": ["Pune", "Mumbai", "Nashik"]
}

df = pd.DataFrame(data)

print(df)