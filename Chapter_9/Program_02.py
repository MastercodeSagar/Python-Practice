"""Chapter_9 - Program 2: handle a conversion error.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

try:
    int("hello")
except ValueError:
    print("2. Conversion error handled")

