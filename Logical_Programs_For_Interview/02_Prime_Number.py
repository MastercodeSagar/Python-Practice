"""Interview logic: prime number.

Definition: A prime number is greater than 1 and has no divisors except 1
and itself.
"""

# Only test divisors up to the square root for a faster check.
number = int(input("Enter a number: "))
is_prime = number > 1
for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
