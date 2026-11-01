"""Interview logic: factorial.

Definition: A factorial multiplies every positive integer from 1 to a number.
For example, 5! is 1 * 2 * 3 * 4 * 5.
"""

# Start at 1 because it is the neutral value for multiplication.
number = int(input("Enter a non-negative number: "))
result = 1
for value in range(2, number + 1):
    result *= value
print("Factorial:", result)
