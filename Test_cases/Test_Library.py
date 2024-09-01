import unittest
from library import Library
from book import Book

class Testlibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
        library.add_book(book)
        self.assertIn(book, library.available_books()) #check book was added

    def test_borrow_book(self):
        library = Library()
        book = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
        library.add_book(book)
        library.borrow_book("9780262313216") # Borrow the book
        self.assertNotIn(book, library.available_books()) # check book is no longer available
        with self.assertRaises(ValueError):
            library.borrow_book("9780262313216")

    def test_return_book(self):
        library = Library()
        book = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
        library.add_book(book)
        library.borrow_book("9780262313216") # borrowd the book
        library.return_book("9780262313216") # retuen the book
        self.assertIn(book, library.available_books()) # check book is available again

    def test_view_available_book(self):
        library = Library()
        book1 = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
        book2 = Book("9781593279288", "Python Crash course", "Eric Matthes", 2016)
        library.add_book(book1)
        library.add_book(book2)
        self.assertIn(book1, library.available_books())
        self.assertIn(book2, library.available_books())
        library.borrow_book("9780262313216") # borrow the book
        self.assertNotIn(book1, library.available_books()) # book should not be available
        self.assertIn(book2, library.available_books()) # book2 is available

if __name__ == "__main__":
    unittest.main()