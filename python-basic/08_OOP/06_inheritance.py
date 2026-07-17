"""
Inheritance
"""

class Animal:

    def sound(self):

        print("Animals make sounds")

class Dog(Animal):

    def bark(self):

        print("Dog Barks")

dog = Dog()

dog.sound()

dog.bark()