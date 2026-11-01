"""Interview logic: bubble sort.

Definition: Bubble sort repeatedly compares neighbouring values and swaps
them when they are in the wrong order.
"""

# Each pass moves the largest remaining value toward the end.
numbers = [5, 1, 4, 2, 8]
for pass_number in range(len(numbers) - 1):
    for index in range(len(numbers) - 1 - pass_number):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
print("Sorted:", numbers)
