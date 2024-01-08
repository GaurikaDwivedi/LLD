from enum import Enum
class FlightStatus(Enum):
    SCHEDULED = 0
    DELAYED = 1
    DEPARTED = 2
    LANDED = 3
    IN_AIR = 4
    ARRIVED = 5
    CANCELLED = 6


class FlightOccurrence:
    def __init__(self, flightNumber, flightDateTime):
        self._assignedGateNumber = None
        self._flightStatus = 0

        self._flightNumber = flightNumber
        self._flightDateTime = flightDateTime

    def getFlightNumber(self):
        return self._flightNumber

    def setFlightNumber(self, flightNumber):
        self._flightNumber = flightNumber

    def getFlightDateTime(self):
        return self._flightDateTime

    def setFlightDateTime(self, flightDateTime):
        self._flightDateTime = flightDateTime

    def getAssignedGateNumber(self):
        return self._assignedGateNumber

    def setAssignedGateNumber(self, assignedGateNumber):
        self._assignedGateNumber = assignedGateNumber

    def getFlightStatus(self):
        return self._flightStatus

    def setFlightStatus(self, flightStatus):
        self._flightStatus = flightStatus

    def equals(self, o):
        if self is o:
            return True
        if o is None or FlightOccurrence != type(o):
            return False
        that = o
        if self._flightDateTime != that._flightDateTime:
            return False
        return self._flightNumber == that._flightNumber

    def hashCode(self):
        result = hash(self._flightNumber)
        result = 31 * result + int((self._flightDateTime ^ (self._flightDateTime >> 32)))
        return result