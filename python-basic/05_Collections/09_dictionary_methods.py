"""
Dictionary Methods
"""

employee = {
    "id":101,
    "name":"Rahul",
    "salary":50000
}

print(employee.keys())

print(employee.values())

print(employee.items())

employee.update({"salary":60000})

print(employee)