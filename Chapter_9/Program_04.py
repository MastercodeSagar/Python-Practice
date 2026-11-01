"""Chapter_9 - Program 4: else runs when no error occurs.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

try:
    result = 12 / 3
except ZeroDivisionError:
    print("4. Error")
else:
    print("4. Result:", result)

