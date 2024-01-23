from enum import Enum
class TableStatus(Enum):
    AVAILABLE = 0
    RESERVED = 1

class Table:
    def __init__(self, tableID, maxCapacity, locationIdentifier, seats):
        self._status = TableStatus.AVAILABLE
        self._currentReservation = None
        self._tableID = tableID
        self._maxCapacity = maxCapacity
        self._locationIdentifier = locationIdentifier
        self._seats = seats

    def checkIsTableAvailable(self):
        return self._status == TableStatus.AVAILABLE

    def getTableID(self):
        return self._tableID

    def setTableID(self, tableID):
        self._tableID = tableID

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def getMaxCapacity(self):
        return self._maxCapacity

    def setMaxCapacity(self, maxCapacity):
        self._maxCapacity = maxCapacity

    def getLocationIdentifier(self):
        return self._locationIdentifier

    def setLocationIdentifier(self, locationIdentifier):
        self._locationIdentifier = locationIdentifier

    def getSeats(self):
        return self._seats

    def setSeats(self, seats):
        self._seats = seats

    def getCurrentReservation(self):
        return self._currentReservation

    def setCurrentReservation(self, currentReservation):
        self._currentReservation = currentReservation