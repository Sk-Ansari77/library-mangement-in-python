import os

DATA_FILE = "library.txt"

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.available else 'Not Available'}"


def load_books():
    books = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                title, author, available = line.strip().split(';')
                books.append(Book(title, author, available == 'True'))
    return books


def save_books(books):
    with open(DATA_FILE, "w") as file:
        for book in books:
            file.write(f"{book.title};{book.author};{book.available}\n")


def list_books(books):
    if books:
        for i, book in enumerate(books):
            print(f"{i + 1}. {book}")
    else:
        print("No books available in the library.")

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    books.append(Book(title, author))
    save_books(books)
    print(f"Book '{title}' by {author} added successfully.")


def borrow_book(books):
    list_books(books)
    book_id = int(input("Enter the number of the book to borrow: ")) - 1
    if 0 <= book_id < len(books):
        if books[book_id].available:
            books[book_id].available = False
            save_books(books)
            print(f"You have borrowed '{books[book_id].title}'.")
        else:
            print("Sorry, that book is currently not available.")
    else:
        print("Invalid book number.")


def return_book(books):
    list_books(books)
    book_id = int(input("Enter the number of the book to return: ")) - 1
    if 0 <= book_id < len(books):
        if not books[book_id].available:
            books[book_id].available = True
            save_books(books)
            print(f"You have returned '{books[book_id].title}'.")
        else:
            print("That book wasn't borrowed.")
    else:
        print("Invalid book number.")

def main():
    books = load_books()
    while True:
        print("\nLibrary Management System")
        print("1. List all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
