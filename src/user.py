class User:
    def __init__(self, username, password, books=[], shelves=[]):
        self.username = username
        self.password = password
        self.books = books
        self.shelves = shelves

    def add_books(self, book, shelf=None):
        self.books.append(book)

    def review_book(self, book, rate):
        book.update_rating(rate)
