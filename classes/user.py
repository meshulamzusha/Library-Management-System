class User:

    def __init__(self, id, name):
        self.user_id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book.isbn)

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            self.borrowed_books.remove(book.isbn)