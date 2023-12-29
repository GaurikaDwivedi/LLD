from library_management.book import Book
class Patron:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.is_available():
            book.check_out()
            self.checked_out_books.append(book)
            print(f"Book has been checked out to {self.name}.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        for i, checked_book in enumerate(self.checked_out_books):
            if checked_book.get_ISBN() == book.get_ISBN():
                book.return_book()
                del self.checked_out_books[i]
                print(f"Book has been returned by {self.name}.")
                return
        print(f"{self.name} did not check out this book.")

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID