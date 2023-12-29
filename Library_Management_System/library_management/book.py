class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = True

    def check_out(self):
        if self.availability:
            self.availability = False
            print("Book has been checked out.")
        else:
            print("Book is not available.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print("Book has been returned.")
        else:
            print("Book has not been checked out.")

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_ISBN(self):
        return self.ISBN

    def is_available(self):
        return self.availability