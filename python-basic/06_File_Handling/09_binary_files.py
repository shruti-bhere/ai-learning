"""
Binary File Example
"""

data = b"Python AI Learning"

with open("binary.dat", "wb") as file:
    file.write(data)

print("Binary file written successfully.")