"""
Encapsulation
"""

class Bank:

    def __init__(self):

        self.__balance = 5000

    def deposit(self,amount):

        self.__balance += amount

    def show_balance(self):

        print("Balance:",self.__balance)

account = Bank()

account.deposit(2000)

account.show_balance()