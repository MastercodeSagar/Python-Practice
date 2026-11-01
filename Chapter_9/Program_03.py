"""Chapter_9 - Program 3: handle division by zero.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

try:
    print(10 / 0)
except ZeroDivisionError:
    print("3. Cannot divide by zero")

