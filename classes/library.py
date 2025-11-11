from classes.book import Book
from classes.user import User


class Library:

    def register_user(self, user):
        self.users[user.user_id] = user
        self.save_data()

    def add_book(self, book):
        self.books[book.isbn] = book
        self.save_data()