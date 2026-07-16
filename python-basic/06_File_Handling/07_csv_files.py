"""
Working with CSV Files
"""

import csv

data = [
    ["Name", "Age"],
    ["Shruti", 22],
    ["Rahul", 25]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(data)

print("CSV file created.")