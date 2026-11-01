"""Beginner project: calculator.

Definition: A calculator accepts values, performs an operation, and displays
the result. This project practises input, conversion, and conditions.
"""

first = float(input("First number: "))
operator = input("Choose +, -, *, or /: ")
second = float(input("Second number: "))

# Select the calculation based on the operator.
if operator == "+":
    answer = first + second
elif operator == "-":
    answer = first - second
elif operator == "*":
    answer = first * second
elif operator == "/" and second != 0:
    answer = first / second
else:
    answer = None

if answer is None:
    print("Invalid operator or division by zero.")
else:
    print("Answer:", answer)
