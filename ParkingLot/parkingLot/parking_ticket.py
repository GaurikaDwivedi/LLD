import time
from enum import Enum


class ParkingTicketStatus(Enum):
    ACTIVE = 0
    PAID = 1


class ParkingTicket:

    def __init__(self, barcode):
        self._vehicle = None
        self._barcode = barcode
        self._ticketIssuingTime = round(time.time() * 1000)
        self._ticketStatus = ParkingTicketStatus.ACTIVE

    def assignTicketTo(self, vehicle):
        self._vehicle = vehicle

    def markAsPaid(self):
        self._ticketStatus = ParkingTicketStatus.PAID

    def getBarcode(self):
        return self._barcode

    def getTicketIssueingTime(self):
        return self._ticketIssuingTime

    def getTicketStatus(self):
        return self._ticketStatus

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != ParkingTicket:
            return False
        that = o
        if self._ticketIssuingTime != that._ticketIssuingTime:
            return False
        return self._barcode == that._barcode

    def hashCode(self):
        result = hash(self._barcode)
        result = 31 * result + int((self._ticketIssuingTime ^ (self._ticketIssuingTime > 32)))
        return result