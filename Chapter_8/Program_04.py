"""Chapter_8 - Program 4: a default parameter.

Beginner definition: A function is a reusable block of code. Parameters provide input and return sends a result back.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

def power(number, exponent=2):
    return number ** exponent
print("4.", power(3), power(2, 3))

