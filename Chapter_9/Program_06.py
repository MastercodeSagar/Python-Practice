"""Chapter_9 - Program 6: write a text file.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

file_name = "chapter_9_notes.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python files are useful.\n")
print("6. File written")

