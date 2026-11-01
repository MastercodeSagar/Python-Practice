"""Chapter_7 - Program 9: update and inspect a dictionary.

Beginner definition: A collection stores multiple values. Lists can change, tuples are fixed, sets contain unique values, and dictionaries use key-value pairs.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

student["passed"] = True
for key, value in student.items():
    print("9.", key, value)
