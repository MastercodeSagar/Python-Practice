"""Chapter_5 - Program 7: find the first multiple.

Beginner definition: A loop repeats code. A for loop is useful when working through a sequence, while repeats while a condition is True.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

for number in range(1, 20):
    if number % 7 == 0:
        print("7. First multiple of 7:", number)
        break

