import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]

students = [50, 20, 15, 15]

plt.pie(students, labels=languages, autopct="%1.1f%%")

plt.title("Programming Language Preference")

plt.show()