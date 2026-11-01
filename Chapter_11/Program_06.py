"""Chapter_11 - Program 6: a class with a default value.

Beginner definition: A class is a blueprint for objects. An object stores data in attributes and performs actions with methods.
Read the comments, run this file, and change one value to observe the result.
"""
# The code below demonstrates the definition in this practical.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance
    def deposit(self, amount):
        self.balance += amount
account = BankAccount("Asha", 100)
account.deposit(50)
print("6. Balance:", account.balance)

