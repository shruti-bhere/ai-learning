"""
Mini Project

Student Management System
"""

class Student:

    def __init__(self, roll, name, marks):

        self.roll = roll

        self.name = name

        self.marks = marks

    def display(self):

        print("\nStudent Details")

        print("Roll :", self.roll)

        print("Name :", self.name)

        print("Marks :", self.marks)

students = []

while True:

    print("\n===== Student Management =====")

    print("1. Add Student")

    print("2. View Students")

    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        roll = input("Enter Roll Number: ")

        name = input("Enter Name: ")

        marks = float(input("Enter Marks: "))

        students.append(Student(roll,name,marks))

        print("Student Added Successfully!")

    elif choice == "2":

        if not students:

            print("No Students Found")

        else:

            for student in students:

                student.display()

    elif choice == "3":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")