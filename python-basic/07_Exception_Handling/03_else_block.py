"""
Else Block
"""

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid Number")

else:
    print("Square:", number * number)