"""Interview logic: Armstrong number.

Definition: An Armstrong number equals the sum of its digits raised to the
power of the number of digits, such as 153 = 1^3 + 5^3 + 3^3.
"""

# Convert to text so the program can inspect each digit separately.
number = int(input("Enter a positive number: "))
digits = str(number)
total = sum(int(digit) ** len(digits) for digit in digits)
print("Armstrong number" if total == number else "Not an Armstrong number")
