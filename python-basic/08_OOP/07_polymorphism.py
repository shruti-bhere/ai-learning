"""
Polymorphism
"""

class Bird:

    def sound(self):

        print("Bird Chirps")

class Cat:

    def sound(self):

        print("Cat Meows")

for animal in [Bird(),Cat()]:

    animal.sound()