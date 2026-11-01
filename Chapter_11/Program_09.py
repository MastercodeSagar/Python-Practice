"""Chapter_11 - Program 9: string representation.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
print("9. Book:", Book("Learn Python"))

