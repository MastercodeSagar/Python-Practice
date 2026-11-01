"""Chapter_12 - Program 8: a generator.

Beginner definition: Advanced tools provide shorter or more flexible ways to process data, repeat work, and extend functions.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

def countdown(limit):
    while limit > 0:
        yield limit
        limit -= 1
print("8.", list(countdown(3)))

