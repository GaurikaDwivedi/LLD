from TicketBookingSystem.Member import Member
from TicketBookingSystem.MovieHall import MovieHall

class TheaterAdministrator(Member):
    def __init__(self, id, name, email, phone):
        self._theaterCompany = None
        super().__init__(id, name, email, phone)

    def addMovie(self, movie, theater):
        theater.addMovie(movie)

    def addShow(self, show, theater):
        theater.addShow(show)
