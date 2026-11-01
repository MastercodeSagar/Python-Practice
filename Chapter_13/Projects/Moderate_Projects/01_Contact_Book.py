"""Moderate project: contact book.

Definition: A contact book stores and retrieves related information. This
project practises dictionaries, loops, functions, and decisions.
"""

contacts = {}


def add_contact():
    name = input("Contact name: ").strip().title()
    phone = input("Phone number: ").strip()
    contacts[name] = phone
    print("Contact saved.")


def find_contact():
    name = input("Search name: ").strip().title()
    print(contacts.get(name, "Contact not found."))


# A loop keeps the menu available until the user chooses to exit.
while True:
    print("\n1. Add  2. Find  3. Show all  4. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "4":
        break
    else:
        print("Choose a valid option.")
