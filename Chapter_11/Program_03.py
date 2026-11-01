"""Chapter_11 - Program 3: an initializer.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class Person:
    def __init__(self, name):
        self.name = name
person = Person("Ravi")
print("3.", person.name)

