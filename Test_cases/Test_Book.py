import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
        self.assertEqual(book.isbn, "9780262313216")
        self.assertEqual(book.title, "Algorithms unlocked")
        self.assertEqual(book.author, "Thomas H. Cormen")
        self.assertEqual(book.year, 2013)

if __name__ == "__main__":
    unittest.main()
