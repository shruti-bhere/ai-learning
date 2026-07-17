"""
Magic Methods
"""

class Student:

    def __init__(self,name):

        self.name = name

    def __str__(self):

        return f"Student Name: {self.name}"

student = Student("Shruti")

print(student)