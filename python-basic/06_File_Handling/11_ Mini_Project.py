"""
Mini Project

Simple Notes Application
"""

filename = "notes.txt"

while True:

    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        note = input("Enter note: ")

        with open(filename, "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":

        try:
            with open(filename, "r") as file:
                print("\nYour Notes:\n")
                print(file.read())

        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")