"""
*args Example
"""

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 90, 70, 85)