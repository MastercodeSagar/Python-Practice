"""Chapter_11 - Program 7: validation in a method.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance


class SafeAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("7. Not enough balance")
safe = SafeAccount("Ravi", 100)
safe.withdraw(150)
