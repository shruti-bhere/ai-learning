"""
Mini Project

Student Result Calculator
"""

def calculate_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print("\n===== Result =====")
    print("Student :", name)
    print("Total   :", total)
    print("Average :", average)
    print("Grade   :", grade)

name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter Marks {i+1}: "))
    marks.append(mark)

calculate_result(name, marks)