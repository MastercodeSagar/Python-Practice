"""Chapter_11 - Program 5: a method changes data.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class Counter:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
counter = Counter()
counter.increase()
print("5. Count:", counter.value)

