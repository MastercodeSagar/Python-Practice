"""Interview logic: Fibonacci sequence.

Definition: Each Fibonacci number is the sum of the two numbers before it.
"""

# Move both sequence values forward after printing the current value.
terms = int(input("How many terms? "))
first, second = 0, 1
for _ in range(terms):
    print(first, end=" ")
    first, second = second, first + second
print()
