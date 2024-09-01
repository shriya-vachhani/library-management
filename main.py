from library import Library
from book import Book

def main():
    library = Library()
    book1 = Book("9780262313216", "Algorithms unlocked", "Thomas H. Cormen", 2013)
    book2 = Book("9781593279288", "Python Crash course", "Eric Matthes", 2016)
    library.add_book(book1)
    library.add_book(book2)

    print("Available Book:")
    for book in library.available_books():
        print(f"{book.title} by {book.author}")

    print("\n Borrowing 'Algorithms unlocked'...")
    library.borrow_book("9780262313216")

    print("\n Available Books after borrowing:")
    for book in library.available_books():
        print(f"{book.title} by {book.author}")

    print("\n Returning 'Algorithms unlocked'...")
    library.return_book("9780262313216")

    print("\n Available Books after returning:")
    for book in library.available_books():
        print(f"{book.title} by {book.author}")

if __name__ == "__main__":
    main()