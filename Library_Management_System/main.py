from time import time, ctime
from library_management.library import Library
from library_management.book import Book
from library_management.patron import Patron
from library_management.checkout import Checkout
def main():
    # create objects of Library, Book, Patron, and Checkout classes
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    patron1 = Patron("John Smith", "123")
    patron2 = Patron("Jane Doe", "456")
    checkout = Checkout()

    # add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # display all books in the library
    library.display_books()

    # check out a book
    checkout.check_out(book1, patron1)

    # get the due date of the checked-out book
    due_date = checkout.get_due_date(book1)
    if due_date is not None:
        print("Due Date:", (due_date))

    # calculate and display the fine for the overdue book
    fine = checkout.calculate_fine(book1)
    if fine > 0:
        print("Fine for overdue book: Rs", fine)

    # display all current checkouts
    checkout.display_checkouts()

    # return a book
    checkout.return_book(book1)

    # display all current checkouts
    checkout.display_checkouts()

if __name__ == "__main__":
    main()
