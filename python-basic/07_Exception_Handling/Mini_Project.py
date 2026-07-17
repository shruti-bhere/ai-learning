"""
Mini Project

ATM System
"""

balance = 5000

try:

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise Exception("Insufficient Balance.")

    balance -= amount

    print("Withdrawal Successful!")
    print("Remaining Balance:", balance)

except ValueError as error:
    print(error)

except Exception as error:
    print(error)

finally:
    print("Thank you for using our ATM.")