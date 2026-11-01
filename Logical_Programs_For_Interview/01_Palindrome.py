"""Interview logic: palindrome.

Definition: A palindrome has the same characters when read forward and
backward, such as "level".
"""

# Remove spaces and compare the text with its reversed form.
text = input("Enter text: ").replace(" ", "").lower()
print("Palindrome" if text == text[::-1] else "Not a palindrome")
