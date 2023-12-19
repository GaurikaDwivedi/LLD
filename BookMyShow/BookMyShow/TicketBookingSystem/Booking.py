import time
from enum import Enum


class BookingStatus(Enum):
    PENDING = 0
    CONFIRMED = 1
    CHECKED_IN = 2
    CANCELED = 3


class Booking:

    def __init__(self, bookingNumber, show, seats, payment):
        self._bookingNumber = bookingNumber
        self._createdOn = round(time.time() * 1000)
        self._status = BookingStatus.PENDING
        self._show = show
        self._seats = seats
        self._payment = payment

    def makePayment(self, payment):
        if payment:
            # Assuming a successful payment
            self._payment = payment
            self._status = BookingStatus.CONFIRMED
            print(f"Payment successful for Booking {self._bookingNumber}")
        else:
            print(f"Payment failed for Booking {self._bookingNumber}. Please try again.")

    def cancel(self):
        if self._status != BookingStatus.CHECKED_IN:
            self._status = BookingStatus.CANCELED
            return True
        return False

    def reserveSeat(self, seat):
        return seat.book()

    def reserveSeats(self, requestedSeats):
        for seat in requestedSeats:
            if not seat.book():
                self._unreserve(self._seats)
                return False
        return True

    def _unreserve(self, seats):
        for seat in seats:
            if not seat.isReserved():
                return
            seat.markAsAvailable()

    def confirmBooking(self):
        if self._status == BookingStatus.PENDING:
            self._status = BookingStatus.CONFIRMED
            return True
        return False

    def checkIn(self):
        if self._status == BookingStatus.CONFIRMED:
            self._status = BookingStatus.CHECKED_IN
            return True
        return False
    
    def refund(self):
        if self._status == BookingStatus.CANCELED and self._payment:
            refund_amount = self._payment.getAmount()
            print(f"Refund of {refund_amount} initiated for Booking {self._bookingNumber}")
            return refund_amount
        else:
            print(f"No refund available for Booking {self._bookingNumber}")
            return 0