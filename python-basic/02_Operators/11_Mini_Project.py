"""
Simple Calculator
"""

print("===== Simple Calculator =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Remainder:", num1 % num2)
else:
    print("Division by zero is not allowed.")

print("Power:", num1 ** num2)