"""
Class Variables
"""

class Student:

    college = "ABC College"

    def __init__(self,name):

        self.name = name

student1 = Student("Shruti")

student2 = Student("Rahul")

print(student1.college)

print(student2.college)