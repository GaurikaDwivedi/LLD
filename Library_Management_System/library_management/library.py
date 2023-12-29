
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book has been added to the library.")

    def remove_book(self, ISBN):
        for i, book in enumerate(self.books):
            if book.get_ISBN() == ISBN:
                del self.books[i]
                print("Book has been removed from the library.")
                return
        print(f"Book with ISBN {ISBN} not found in the library.")

    def search_book(self, ISBN):
        for book in self.books:
            if book.get_ISBN() == ISBN:
                return book
        print(f"Book with ISBN {ISBN} not found in the library.")
        return None

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("ISBN:", book.get_ISBN())
            print("Availability:", "Available" if book.is_available() else "Checked out")
            print()
