from datetime import datetime, timedelta

class Checkout:
    def __init__(self):
        self.checkouts = {}
        self.DAY_SECONDS = 60 * 60 * 24
        self.MAX_FINE = 10

    def check_out(self, book, patron):
        if book.is_available():
            patron.check_out_book(book)
            due_date = datetime.now() + timedelta(days=7)  # 7 days from current time
            self.checkouts[book] = (patron, due_date)
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.checkouts:
            patron, _ = self.checkouts[book]
            patron.return_book(book)
            del self.checkouts[book]
        else:
            print("Book has not been checked out.")

    def display_checkouts(self):
        print("Current checkouts:")
        for book, (patron, due_date) in self.checkouts.items():
            print("Book:", book.get_title())
            print("Author:", book.get_author())
            print("Patron:", patron.get_name())
            print("Due Date:", due_date.strftime("%Y-%m-%d %H:%M:%S"))
            print()

    def get_due_date(self, book):
        if book in self.checkouts:
            return self.checkouts[book][1]
        else:
            print("Book has not been checked out.")
            return None

    def calculate_fine(self, book):
        due_date = self.get_due_date(book)
        current_date = datetime.now()
        overdue_duration = current_date - due_date

        if overdue_duration.total_seconds() < 0:
            # Book was returned early, no fine
            return 0.0
        else:
            # Calculate fine based on how many days late the book is
            days_late = overdue_duration.days
            fine = days_late * 0.50
            # Cap the fine at MAX_FINE
            return min(fine, self.MAX_FINE)