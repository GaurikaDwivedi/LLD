class Movie:
    def __init__(self, title, description, durationInMins, language, releaseDate, genre, movieAddedBy):
        self._shows = []
        self._title = title
        self._description = description
        self._durationInMins = durationInMins
        self._language = language
        self._releaseDate = releaseDate
        self._genre = genre
        self._movieAddedBy = movieAddedBy

    def getTitle(self):
        return self._title

    def updateTitle(self, title):
        self._title = title

    def getDescription(self):
        return self._description

    def updateDescription(self, description):
        self._description = description

    def getDurationInMins(self):
        return self._durationInMins

    def updateDurationInMins(self, durationInMins):
        self._durationInMins = durationInMins

    def getLanguage(self):
        return self._language

    def updateLanguage(self, language):
        self._language = language

    def getReleaseDate(self):
        return self._releaseDate

    def updateReleaseDate(self, releaseDate):
        self._releaseDate = releaseDate

    def getGenre(self):
        return self._genre

    def updateGenre(self, genre):
        self._genre = genre

    def getMovieAddedBy(self):
        return self._movieAddedBy

    def updateMovieAddedBy(self, movieAddedBy):
        self._movieAddedBy = movieAddedBy

    def getShows(self):
        return self._shows

    def adShow(self, show):
        self._shows.append(show)