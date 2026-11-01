"""Advanced project: library management system.

Definition: A management system stores records and applies rules to them.
This project practises classes, lists, methods, and validation.
"""


class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def borrow(self):
        if not self.is_available:
            return False
        self.is_available = False
        return True

    def return_book(self):
        self.is_available = True


library = [Book("Python Basics"), Book("Learning Loops")]
title = input("Book title to borrow: ").strip().lower()

for book in library:
    if book.title.lower() == title:
        print("Borrowed." if book.borrow() else "Already borrowed.")
        break
else:
    print("Book not found.")
