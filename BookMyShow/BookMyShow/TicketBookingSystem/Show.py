import time

class Show:
    def __init__(self, showId, startTime, playingAt, movie):
        self._showId = showId
        self._createdOn = round(time.time() * 1000)
        self._startTime = startTime
        self._playingAt = playingAt
        self._movie = movie
        self._durationInMin = movie.getDurationInMins()

    def getShowId(self):
        return self._showId

    def setShowId(self, showId):
        self._showId = showId

    def getCreatedOn(self):
        return self._createdOn

    def setCreatedOn(self, createdOn):
        self._createdOn = createdOn

    def getStartTime(self):
        return self._startTime

    def setStartTime(self, startTime):
        self._startTime = startTime

    def getDurationInMin(self):
        return self._durationInMin

    def setDurationInMin(self, durationInMin):
        self._durationInMin = durationInMin

    def getPlayingAt(self):
        return self._playingAt

    def setPlayingAt(self, playingAt):
        self._playingAt = playingAt

    def getMovie(self):
        return self._movie

    def setMovie(self, movie):
        self._movie = movie

    def getShowInfo(self):
        return f"Show ID: {self._showId}, Movie: {self._movie.getTitle()}, Start Time: {self._startTime}, Playing At: {self._playingAt._name}"

