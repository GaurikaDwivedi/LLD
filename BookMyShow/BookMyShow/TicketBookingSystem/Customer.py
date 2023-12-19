from TicketBookingSystem.Member import Member


class Customer(Member):
    def __init__(self, name, email, phone):
        self._currentBookings = []
        id = 0
        super().__init__(id, name, email, phone)

    def makeBooking(self, booking):
        if all(not seat.isReserved() for seat in booking._seats):
            # All seats are available, proceed with the booking
            booking.makePayment(booking._payment)
            booking.confirmBooking()

            # Mark seats as reserved
            for seat in booking._seats:
                seat.book()
            self._currentBookings.append(booking)
            print(f"Booking successful!, Seat Numbers are: {[seat.getSeatId() for seat in booking._seats]}")
        else:
            # Seats are already reserved, inform the user
            print("Some or all selected seats are already booked. Please choose different seats.")


    def getBookings(self):
        return self._currentBookings

    def cancelBooking(self, booking):
        if booking in self._currentBookings:
            # Cancel the booking if it exists in the current bookings
            booking.cancel()
            print(f"Booking {booking._bookingNumber} canceled.")
            # Mark seats as available
            booking._unreserve(booking._seats)
            # Remove the booking from the current bookings
            self._currentBookings.remove(booking)
        else:
            print("Booking not found.")

