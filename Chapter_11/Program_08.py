"""Chapter_11 - Program 8: inheritance.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate
savings = SavingsAccount("Mira", 200)
savings.add_interest(0.10)
print("8. Interest balance:", savings.balance)
