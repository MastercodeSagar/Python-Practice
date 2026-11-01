"""Beginner project: unit converter.

Definition: A converter changes a value from one unit to another using a
formula.
"""

kilometres = float(input("Distance in kilometres: "))
miles = kilometres * 0.621371

# Round the result so it is easier to read.
print(f"Distance in miles: {miles:.2f}")
