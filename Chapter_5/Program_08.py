"""Chapter_5 - Program 8: skip odd numbers.

Beginner definition: A loop repeats code. A for loop is useful when working through a sequence, while repeats while a condition is True.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

for number in range(1, 6):
    if number % 2 != 0:
        continue
    print("8.", number)

