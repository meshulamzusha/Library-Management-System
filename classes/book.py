class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, isbn: {self.isbn}, available: {self.is_available}"
