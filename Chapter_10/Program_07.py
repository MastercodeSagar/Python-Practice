"""Chapter_10 - Program 7: work with paths.

Beginner definition: A module is a Python file that provides reusable code. The standard library contains modules included with Python.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

from pathlib import Path
current_file = Path(__file__)
print("7. File name:", current_file.name)

