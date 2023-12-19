class MovieHall:
    def __init__(self, owningCompany, name, shows, moviesCurrentlyPlaying):
        self._owningCompany = None
        self._name = None
        self._shows = set()
        self._moviesCurrentlyPlaying = set()

        self._owningCompany = owningCompany
        self._name = name

    def addShow(self, show):
        self._shows.add(show)

    def addMovie(self, movie):
        self._moviesCurrentlyPlaying.add(movie)

    def removeMovie(self, movie):
        if movie not in self._shows:
            self._moviesCurrentlyPlaying.remove(movie)
            return True
        return False

    def removeShow(self, show):
        if show not in self._shows:
            self._shows.remove(show)
            return True
        return False
    def getShows(self):
        return self._shows