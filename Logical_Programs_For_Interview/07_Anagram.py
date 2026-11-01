"""Interview logic: anagram.

Definition: Two words are anagrams when they contain the same letters with
the same counts, such as "listen" and "silent".
"""

# Sorting both words makes equal letters appear in the same order.
first = sorted(input("First word: ").replace(" ", "").lower())
second = sorted(input("Second word: ").replace(" ", "").lower())
print("Anagrams" if first == second else "Not anagrams")
