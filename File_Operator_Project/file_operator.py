import os
from datetime import datetime


# Journal Manager Class
class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Create a new file using x mode
    def create_file(self):
        try:
            with open(self.filename, "x") as file:
                print("Journal file created successfully.")

        except FileExistsError:
            pass

        except PermissionError:
            print("Permission denied. Cannot create the file.")

        except OSError as error:
            print("File error:", error)

    # Add a new entry using a mode
    def add_entry(self):
        try:
            entry = input("Write your journal entry: ")

            if not entry.strip():
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write("Timestamp: " + timestamp + "\n")
                file.write("Entry: " + entry + "\n\n")

            print("Journal entry added successfully.")

        except PermissionError:
            print("Permission denied. Cannot write to the file.")

        except OSError as error:
            print("File error:", error)

    # View all entries using r mode
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if content:
                print("\n--- All Journal Entries ---")
                print(content)
            else:
                print("No journal entries found.")

        except FileNotFoundError:
            print("Journal file not found. Add an entry first.")

        except PermissionError:
            print("Permission denied. Cannot read the file.")

        except OSError as error:
            print("File error:", error)

    # Search an entry using r mode
    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                entries = file.readlines()

            found = False

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry, end="")
                    found = True

            if not found:
                print("No matching entry found.")

        except FileNotFoundError:
            print("Journal file not found.")

        except PermissionError:
            print("Permission denied. Cannot read the file.")

        except OSError as error:
            print("File error:", error)

    # Delete all entries using w mode
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("Journal file does not exist.")
                return

            confirm = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirm.lower() == "yes":
                with open(self.filename, "w") as file:
                    pass

                os.remove(self.filename)
                print("All journal entries deleted successfully.")

            else:
                print("Deletion cancelled.")

        except PermissionError:
            print("Permission denied. Cannot delete the file.")

        except OSError as error:
            print("File error:", error)


# Main Program
journal = JournalManager()

# Create journal file if it does not exist
journal.create_file()

while True:
    print("\n--- Personal Journal Menu ---")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")