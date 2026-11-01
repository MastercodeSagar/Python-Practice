"""Chapter_9 - Program 1: catch invalid number input.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

try:
    number = int("25")
    print("1.", number)
except ValueError:
    print("1. Invalid number")

