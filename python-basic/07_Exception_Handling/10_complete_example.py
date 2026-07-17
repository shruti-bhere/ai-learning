"""
Complete Example
"""

try:

    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))

    print("Division:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Calculation completed successfully.")

finally:
    print("Program Ended.")