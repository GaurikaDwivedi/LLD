from flight_reservation_system.user import User
class Customer(User):
    def __init__(self, name, address, email, phone, frequentFlyerNumber):
        self.itineraries = None
        self._passportNumber = None
        self._dateOfBirth = None

        super().__init__(name, address, email, phone)
        self._frequentFlyerNumber = frequentFlyerNumber

    def cancelReservation(self, reservation):
        return reservation.cancel()

    def makeReservationAndGetItinerary(self, reservation, transactionId):
        print(f"{self.getName()} is making reservation.")
        return reservation.makePaymentAndCompleteBooking(transactionId)

    def getFrequentFlyerNumber(self):
        return self._frequentFlyerNumber

    def setFrequentFlyerNumber(self, frequentFlyerNumber):
        self._frequentFlyerNumber = frequentFlyerNumber

    def getItineraries(self):
        return self.itineraries

    def setItineraries(self, itineraries):
        self.itineraries = itineraries

    def getPassportNumber(self):
        return self._passportNumber
    
    def setPassportNumber(self, passportNumber):
        self._passportNumber = passportNumber

    def getDateOfBirth(self):
        return self._dateOfBirth

    def setDateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Customer:
            return False
        customer = o
        return self._frequentFlyerNumber == customer._frequentFlyerNumber

    def hashCode(self):
        return hash(self._frequentFlyerNumber)