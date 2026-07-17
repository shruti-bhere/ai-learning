import matplotlib.pyplot as plt

students = ["Shruti", "Rahul", "Priya", "Amit"]

marks = [85, 72, 90, 80]

plt.bar(students, marks)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()