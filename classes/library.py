from classes.book import Book
from classes.user import User
import json
import os 

class Library:
  
    def __init__(self, data_file="data.json"):
        self.books = {}
        self.users = {}
        self.data_file = data_file
        self.load_data()

    def register_user(self, user):
        self.users[user.user_id] = user
        self.save_data()

    def add_book(self, book):
        self.books[book.isbn] = book
        self.save_data()

    def borrow_book(self, user_id, isbn):
        if user_id not in self.users:
            raise Exception("User not found")
        if isbn not in self.books:
            raise Exception("Book not found")
        book = self.books[isbn]
        if book.is_available:
            book.is_available = False
            self.users[user_id].borrow_book(book)
            self.save_data()
        else:
            print("Book already borrowed")

    def return_book(self, user_id, isbn):
        if user_id not in self.users:
            raise Exception("User not found")
        if isbn not in self.books:
            raise Exception("Book not found")
        book = self.books[isbn]
        if not book.is_available:
            book.is_available = True
            self.users[user_id].return_book(book)
            self.save_data()
        else:
            print("Book was not borrowed")

    def save_data(self):
        data = {
            "books": [b.to_dict() for b in self.books.values()],
            "users": [u.to_dict() for u in self.users.values()]
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return
                data = json.loads(content)
                for b in data.get("books", []):
                    book = Book.from_dict(b)
                    self.books[book.isbn] = book
                for u in data.get("users", []):
                    user = User.from_dict(u)
                    self.users[user.user_id] = user
        except json.JSONDecodeError:
            print(f"{self.data_file} empty or not valid json")


    def search_book(self, query):
        results = []
        q = query.lower()
        for book in self.books.values():
            if q in book.title.lower() or q in book.author.lower():
                results.append(book)
        return results

    def list_available_books(self):
        available = [book for book in self.books.values() if book.is_available]
        return available

