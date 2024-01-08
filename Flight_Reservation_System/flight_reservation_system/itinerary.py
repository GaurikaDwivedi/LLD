class Itinerary:
    def __init__(self, confirmationNumber, primaryTraveller, flights, seats, creationDateTime):
        self._confirmationNumber = confirmationNumber
        self._primaryTraveller = primaryTraveller
        self._flights = flights
        self._seats = seats
        self._creationDateTime = creationDateTime

    def getConfirmationNumber(self):
        return self._confirmationNumber

    def getPrimaryTraveller(self):
        return self._primaryTraveller

    def getFlights(self):
        return self._flights

    def getSeats(self):
        return self._seats

    def getCreationDateTime(self):
        return self._creationDateTime
