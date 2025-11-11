from classes.book import Book
from classes.user import User


class Library:

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
