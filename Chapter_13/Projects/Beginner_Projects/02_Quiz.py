"""Beginner project: quiz.

Definition: A quiz asks questions, checks answers, and keeps a score.
"""

questions = {
    "What keyword creates a function? ": "def",
    "What type stores True or False? ": "bool",
    "What file extension does Python use? ": ".py",
}
score = 0

# Visit every question and compare a normalised answer.
for question, correct_answer in questions.items():
    answer = input(question).strip().lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Correct answer:", correct_answer)

print(f"Final score: {score}/{len(questions)}")
