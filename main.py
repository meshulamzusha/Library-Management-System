from classes.library import Library

def main():
    lib = Library()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. List Available Books")
        print("7. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            lib.add_book(book)
            print(f"Book '{title}' added!")

        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user = User(user_id, name)
            lib.register_user(user)
            print(f"User '{name}' registered!")

        elif choice == "3":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            try:
                lib.borrow_book(user_id, isbn)
                print(f"User '{user_id}' borrowed book '{isbn}'!")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            try:
                lib.return_book(user_id, isbn)
                print(f"User '{user_id}' returned book '{isbn}'!")
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            query = input("Enter book title or author to search: ")
            results = lib.search_book(query)
            if results:
                print("Search results:")
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            available_books = lib.list_available_books()
            if available_books:
                print("Available books:")
                for b in available_books:
                    print(b)
            else:
                print("No books available.")

        elif choice == "7":
            lib.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice, try again.")