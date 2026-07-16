"""
Student Marks Analysis using NumPy
"""

import numpy as np

marks = np.array([85, 90, 78, 92, 88, 76, 95])

print("Student Marks:", marks)

print("Highest Marks:", np.max(marks))

print("Lowest Marks:", np.min(marks))

print("Average Marks:", np.mean(marks))

print("Median Marks:", np.median(marks))

print("Standard Deviation:", np.std(marks))

print("Sorted Marks:", np.sort(marks))