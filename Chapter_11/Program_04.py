"""Chapter_11 - Program 4: an instance method.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class Greeting:
    def __init__(self, name):
        self.name = name
    def say(self):
        return f"Hello, {self.name}!"
print("4.", Greeting("Mira").say())

