"""Chapter_13 - Program 10: mini quiz.

Beginner definition: A project combines several Python concepts to solve a small, realistic problem.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

questions = {"2 + 2": "4", "Python file extension": ".py"}
score = 0
for question, answer in questions.items():
    user_answer = answer  # Replace with input(question + ": ") to play.
    if user_answer == answer:
        score += 1
print(f"10. Quiz score: {score}/{len(questions)}")
