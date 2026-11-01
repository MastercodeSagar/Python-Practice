"""Chapter_12 - Program 9: a simple decorator.

Beginner definition: Advanced tools provide shorter or more flexible ways to process data, repeat work, and extend functions.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

def announce(function):
    def wrapped():
        print("Starting")
        function()
        print("Finished")
    return wrapped
@announce
def say_hello():
    print("9. Hello")
say_hello()

