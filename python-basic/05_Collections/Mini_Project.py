"""
Student Management System
"""

students = {}

while True:

    print("\n===== Student Management =====")

    print("1. Add Student")

    print("2. View Students")

    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = input("Roll Number: ")

        name = input("Name: ")

        marks = float(input("Marks: "))

        students[roll] = {
            "name":name,
            "marks":marks
        }

        print("Student Added Successfully!")

    elif choice == "2":

        if not students:
            print("No Students Found")

        else:

            for roll,data in students.items():

                print(f"Roll: {roll}")

                print(f"Name: {data['name']}")

                print(f"Marks: {data['marks']}")

                print("-"*30)

    elif choice=="3":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")