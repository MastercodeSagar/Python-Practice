"""Interview logic: linear search.

Definition: Linear search checks each list item from left to right until it
finds the target or reaches the end.
"""

# enumerate gives us both the position and the value.
numbers = [12, 45, 7, 23, 18]
target = int(input("Number to find: "))
position = -1
for index, number in enumerate(numbers):
    if number == target:
        position = index
        break
print("Index:", position)
