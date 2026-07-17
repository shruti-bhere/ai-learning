"""
Common Exceptions
"""

try:
    data = [10, 20, 30]

    print(data[5])

except IndexError:
    print("Index Out of Range")