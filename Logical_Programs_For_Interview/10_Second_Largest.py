"""Interview logic: second-largest value.

Definition: The second-largest unique value is the value just below the
largest value after duplicates are removed.
"""

# Convert to a set first so duplicate values do not affect the answer.
numbers = [10, 25, 8, 25, 17]
unique_numbers = sorted(set(numbers))
if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("At least two unique values are required.")
