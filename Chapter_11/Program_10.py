"""Chapter_11 - Program 10: multiple objects.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


books = [Book("Loops"), Book("Functions")]
print("10. Books:", [str(book) for book in books])
