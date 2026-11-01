"""Chapter_9 - Program 9: JSON text.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

import json
profile = {"name": "Asha", "completed": 8}
json_text = json.dumps(profile, indent=2)
print("9.", json_text)

