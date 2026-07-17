"""
Instance Variables
"""

class Car:

    def __init__(self, brand, model):

        self.brand = brand

        self.model = model

car1 = Car("Toyota","Fortuner")

car2 = Car("Tesla","Model 3")

print(car1.brand)

print(car2.brand)