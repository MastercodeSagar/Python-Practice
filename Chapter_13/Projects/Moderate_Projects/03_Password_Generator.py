"""Moderate project: password generator.

Definition: A password generator creates a random string from safe character
groups. This project practises modules, strings, and loops.
"""

import secrets
import string

length = int(input("Password length (at least 8): "))
if length < 8:
    print("Use a length of at least 8.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    # secrets is designed for stronger random values than random.
    password = "".join(secrets.choice(characters) for _ in range(length))
    print("Generated password:", password)
