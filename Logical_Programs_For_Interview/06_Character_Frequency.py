"""Interview logic: character frequency.

Definition: Frequency tells how many times each character appears.
"""

# A dictionary stores each character and its running count.
text = input("Enter text: ").lower()
frequency = {}
for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1
print(frequency)
