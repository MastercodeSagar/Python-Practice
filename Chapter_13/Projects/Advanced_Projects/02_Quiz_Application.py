"""Advanced project: JSON quiz application.

Definition: A data-driven application reads structured data and uses it to
perform a task. This project practises JSON, files, functions, and scoring.
"""

import json

questions_json = """[
    {"question": "What does len() return?", "answer": "length"},
    {"question": "What keyword starts a loop over a sequence?", "answer": "for"}
]"""
questions = json.loads(questions_json)


def run_quiz(items):
    score = 0
    for item in items:
        answer = input(item["question"] + " ").strip().lower()
        if answer == item["answer"]:
            score += 1
            print("Correct")
        else:
            print("Answer:", item["answer"])
    return score


score = run_quiz(questions)
print(f"Score: {score}/{len(questions)}")
