"""
Custom Exception
"""

class InvalidAgeError(Exception):
    pass

age = int(input("Enter Age: "))

if age < 18:
    raise InvalidAgeError("Invalid Age!")

print("Eligible")