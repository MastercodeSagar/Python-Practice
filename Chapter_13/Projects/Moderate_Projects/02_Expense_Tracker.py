"""Moderate project: expense tracker.

Definition: An expense tracker records spending and calculates totals. This
project practises lists, dictionaries, functions, and numeric input.
"""

expenses = []


def add_expense():
    category = input("Category: ").strip().title()
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Enter a number.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    expenses.append({"category": category, "amount": amount})


add_expense()
add_expense()
total = sum(item["amount"] for item in expenses)
print("Expenses:", expenses)
print(f"Total: {total:.2f}")
