"""
Random Module
"""

import random

print(random.randint(1,100))

fruits = ["Apple","Banana","Mango","Orange"]

print(random.choice(fruits))

random.shuffle(fruits)

print(fruits)