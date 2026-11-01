"""Chapter_9 - Program 7: read a whole file.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

with open(file_name, "r", encoding="utf-8") as file:
    print("7.", file.read().strip())

