import time
from enum import Enum

class ReservationStatus(Enum):
    REQUESTED = 0
    RESERVED =1
    CHECKED_IN = 2
    CANCELED = 3
    
class Reservation:

    def __init__(self, reservationID):
        self._peopleCount = 0
        self._checkinTime = 0
        self._customer = None
        self._tables = None
        self._notificationsSent = None
        self._customer = None
        self._reservationID = reservationID
        self._timeOfReservation = round(time.time() * 1000)
        self._status = ReservationStatus.REQUESTED

    def updatePeopleCount(self, count):
        self._peopleCount = count
    
    def getStatus(self):
        return self._status
    
    def updateStatus(self, status):
        self._status = status
    
    def getPeopleCount(self):
        return self._peopleCount
    
    def getReservationID(self):
        return self._reservationID
    
    def cancelReservation(self):
        if self._status == ReservationStatus.REQUESTED or self._status == ReservationStatus.RESERVED:
            self._status = ReservationStatus.CANCELED
            return True
        return False
    
    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Reservation:
            return False
        that = o
        return self._reservationID == that._reservationID

    def hashCode(self):
        return self._reservationID