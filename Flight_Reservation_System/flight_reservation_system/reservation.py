import time
from enum import Enum
from flight_reservation_system.itinerary import Itinerary
from flight_reservation_system.payment import Payment, PaymentStatus
class ReservationStatus(Enum):
    PENDING = 0
    CONFIRMED = 1
    CANCELLED = 2

class Reservation:
    def __init__(self, confirmationNumber, primaryTraveller, flights, seats, passengers):
        self._confirmationNumber = confirmationNumber
        self._primaryTraveller = primaryTraveller
        self._flights = flights
        self._seats = seats
        self._creationDateTime = round(time.time() * 1000)
        self._status = ReservationStatus.PENDING
        self._checkInStatus = {}
        self._passengers = passengers
        self._payment = None

    def makePaymentAndCompleteBooking(self, transactionId):
        self._status = ReservationStatus.CONFIRMED
        payment = Payment(transactionId, self)
        self._payment = payment
        print(f"Payment is in Progress!!\n Please wait...")
        payment.setPaymentStatus(PaymentStatus.PAID)
        print(f"Payment status: {self._payment.getPaymentStatus().name},Booking Status: {self.getStatus().name}")
        itinerary = Itinerary(
            confirmationNumber=self._confirmationNumber,
            primaryTraveller=self._primaryTraveller,
            flights=self._flights,
            seats=self._seats,
            creationDateTime=self._creationDateTime
        )
        self.getPrimaryTraveller().setItineraries(itinerary)
        return self.getPrimaryTraveller().getItineraries()

    def cancel(self):
        if self._payment:
             self._payment.setPaymentStatus(PaymentStatus.REFUNDED)
        self._status = ReservationStatus.CANCELLED
        message = f"{self.getConfirmationNumber()} Booking Cancelled. Payment Status: {self._payment.getPaymentStatus().name}"
        return message

    def getConfirmationNumber(self):
        return self._confirmationNumber
    
    def setConfirmationNumber(self, confirmationNumber):
        self._confirmationNumber = confirmationNumber

    def getPrimaryTraveller(self):
        return self._primaryTraveller

    def setPrimaryTraveller(self, primaryTraveller):
        self._primaryTraveller = primaryTraveller

    def getFlights(self):
        return self._flights

    def setFlights(self, flights):
        self._flights = flights

    def getSeats(self):
        return self._seats

    def setSeats(self, seats):
        self._seats = seats

    def getCreationDateTime(self):
        return self._creationDateTime

    def setCreationDateTime(self, creationDateTime):
        self._creationDateTime = creationDateTime

    def getStatus(self):
        return self._status
    
    def setStatus(self, status):
        self._status = status

    def getCheckInStatus(self):
        return self._checkInStatus

    def checkin(self, passenger, flight):
        if passenger not in self._checkInStatus.keys():
            self._checkInStatus[passenger] = {}
        flightCheckinStatus = self._checkInStatus[passenger]
        flightCheckinStatus[flight] = True

    def getPassengers(self):
        return self._passengers

    def setPassengers(self, passengers):
        self._passengers = passengers