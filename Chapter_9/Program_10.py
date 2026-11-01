"""Chapter_9 - Program 10: load JSON text.

Beginner definition: An exception is an error that happens while a program runs. Files store data so it can be used later.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

import json

json_text = '{"name": "Asha", "completed": 8}'
loaded = json.loads(json_text)
print("10. Loaded name:", loaded["name"])
