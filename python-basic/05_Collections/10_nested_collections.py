"""
Nested Collections
"""

students = [
    {
        "name":"Shruti",
        "marks":[90,88,91]
    },
    {
        "name":"Rahul",
        "marks":[80,82,84]
    }
]

for student in students:

    average = sum(student["marks"])/len(student["marks"])

    print(student["name"],average)