"""
Working with JSON Files
"""

import json

student = {
    "name": "Shruti",
    "course": "AI",
    "age": 22
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")