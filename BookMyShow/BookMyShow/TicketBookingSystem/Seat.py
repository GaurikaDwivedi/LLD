from enum import Enum


class SeatType(Enum):
    REGULAR = 0
    PREMIUM = 1
    ACCESSIBLE = 2
    RECLINER = 3


class Seat:

    def __init__(self,seatId, price):
        self._seatId = seatId
        self._isReserved = False
        self._price = price
        self._show = None

    def book(self):
        if not self._isReserved:
            self._isReserved = True
            return True
        return False

    def markAsAvailable(self):
        self._isReserved = False

    def getSeatId(self):
        return self._seatId

    def isReserved(self):
        return self._isReserved

    def getPrice(self):
        return self._price

    def updatePrice(self, price):
        self._price = price

    def getShow(self):
        return self._show

    def updateShow(self, show):
        self._show = show

    @classmethod
    def get_available_seats(cls, seats):
        return [seat for seat in seats if not seat.isReserved()]
    
    def __str__(self):
        return f"Seat {self._seatId} - {'Reserved' if self._isReserved else 'Available'}"
