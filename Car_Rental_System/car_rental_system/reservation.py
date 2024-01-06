import time

class Reservation:
    def __init__(self, reservationNumber, returnDate, primaryDriver, pickupLocation, dropOffLocation, vehicle):
        self._secondaryDrivers = None
        self._insurance = None
        self._reservationNumber = reservationNumber
        self._creationDate = round(time.time() * 1000)
        self._returnDate = returnDate
        self._primaryDriver = primaryDriver
        self._pickupLocation = pickupLocation
        self._dropOffLocation = dropOffLocation
        self._vehicle = vehicle

    def addSecondaryDriver(self, secondaryDriver):
        self._secondaryDrivers.append(secondaryDriver)

    def _extendReservation(self, newEndDate):
        self._returnDate = newEndDate

    def getReservationNumber(self):
        return self._reservationNumber

    def getCreationDate(self):
        return self._creationDate

    def getReturnDate(self):
        return self._returnDate

    def updateReturnDate(self, returnDate):
        self._returnDate = returnDate

    def getPickupLocation(self):
        return self._pickupLocation

    def updatePickupLocation(self, pickupLocation):
        self._pickupLocation = pickupLocation

    def getDropOffLocation(self):
        return self._dropOffLocation

    def updateDropOffLocation(self, dropOffLocation):
        self._dropOffLocation = dropOffLocation

    def getPrimaryDriver(self):
        return self._primaryDriver

    def updatePrimaryDriver(self, primaryDriver):
        self._primaryDriver = primaryDriver

    def getSecondaryDrivers(self):
        return self._secondaryDrivers

    def setSecondaryDrivers(self, secondaryDrivers):
        self._secondaryDrivers = secondaryDrivers

    def getVehicle(self):
        return self._vehicle

    def changeVehicle(self, vehicle):
        self._vehicle = vehicle

    def getInsurance(self):
        return self._insurance

    def changeInsurance(self, insurance):
        self._insurance = insurance