class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return title
