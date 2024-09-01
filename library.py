# create a class library

class Library:
    def __init__(self):
        self.book = [] #store available book
        self.borrowed_books = {} # to store borrowed books with ISBN number

    def add_book(self, book):
        self.book.append(book) #add book

    def borrow_book(self, isbn):
        book_to_borrow = None
        for book in self.book:
            if book.isbn == isbn:
                if isbn in self.borrowed_books:
                    raise ValueError("Book is already borrowed")
                self.borrowed_books[isbn] = book
                book_to_borrow = book
                break

        if book_to_borrow:
            self.book.remove(book_to_borrow)
        else:
            raise ValueError("Book not found")

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            book = self.borrowed_books.pop(isbn) # removed from borrow books
            self.book.append(book) # add back to book list
        else:
            raise ValueError("Book not borrowed")

    def available_books(self):
        return self.book # list of available book



