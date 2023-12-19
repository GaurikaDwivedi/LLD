# Import necessary classes
from TicketBookingSystem.Member import Member
from TicketBookingSystem.Customer import Customer
from TicketBookingSystem.FrontDeskAssistant import FrontDeskAssistant
from TicketBookingSystem.TheaterAdministrator import TheaterAdministrator
from TicketBookingSystem.SystemAdministrator import SystemAdministrator
from TicketBookingSystem.MovieHall import MovieHall
from TicketBookingSystem.Show import Show
from TicketBookingSystem.Seat import Seat
from TicketBookingSystem.Address import Address
from TicketBookingSystem.Movie import Movie
from TicketBookingSystem.Booking import Booking, BookingStatus
from TicketBookingSystem.Payment import Payment, PaymentStatus, PaymentMethod
from TicketBookingSystem.System import System

# Instantiate Member
member1 = Member(id=1, name="John Doe", email="john.doe@example.com", phone="123-456-7890")

# Instantiate Customer
customer1 = Customer(name="Customer Name 1", email="customer1@example.com", phone="987-654-3210")
customer2 = Customer(name="Customer Name 2", email="customer2@example.com", phone="987-654-3211")
# Instantiate FrontDeskAssistant
front_desk_assistant = FrontDeskAssistant(id=2, name="Front Desk Assistant", email="front.desk@example.com", phone="111-222-3333")

# Instantiate TheaterAdministrator
theater_administrator = TheaterAdministrator(id=3, name="Theater Admin", email="theater.admin@example.com", phone="444-555-6666")

# Instantiate SystemAdministrator
my_system = System()
system_administrator = SystemAdministrator(system=my_system, id=4, name="System Admin", email="system.admin@example.com", phone="777-888-9999")

# Instantiate MovieHall
movie_hall1 = MovieHall(owningCompany=theater_administrator, name="Hall 1", shows=set(), moviesCurrentlyPlaying=set())
movie_hall2 = MovieHall(owningCompany=theater_administrator, name="Hall 2", shows=set(), moviesCurrentlyPlaying=set())
# Instantiate Show
movie1 = Movie(title="Inception", description="Mind-bending movie", durationInMins=150, language="English", releaseDate="2022-01-01", genre="Sci-Fi", movieAddedBy=system_administrator)
movie2 = Movie(title="Inception", description="Mind-bending movie", durationInMins=150, language="English", releaseDate="2022-01-01", genre="Sci-Fi", movieAddedBy=system_administrator)
movie3 = Movie(title="The Shawshank Redemption", description="Drama about prison life", durationInMins=142,
                language="English", releaseDate="2023-02-15", genre="Drama", movieAddedBy=None)

movie4 = Movie(title="The Dark Knight", description="Superhero action film", durationInMins=152, language="English",
               releaseDate="2023-03-10", genre="Action", movieAddedBy=None)

movie5 = Movie(title="Forrest Gump", description="Epic journey of a simple man", durationInMins=142, language="English",
               releaseDate="2023-04-05", genre="Drama", movieAddedBy=None)

show1 = Show(showId=1, startTime="2022-01-01 18:00", playingAt=movie_hall1, movie=movie1)
show2 = Show(showId=2, startTime="2022-01-01 19:00", playingAt=movie_hall2, movie=movie2)
show3 = Show(showId=3, startTime="2022-01-01 21:30", playingAt=movie_hall1, movie=movie5)
show4 = Show(showId=4, startTime="2022-01-01 9:45", playingAt=movie_hall2, movie=movie4)
show5 = Show(showId=5, startTime="2022-01-01 9:30", playingAt=movie_hall1, movie=movie3)
movie_hall1.addShow(show1)
movie_hall2.addShow(show2)
movie_hall2.addShow(show4)
movie_hall1.addShow(show3)
movie_hall1.addShow(show5)

# Instantiate Address
address = Address(streetAddress="123 Main St", city="City", state="State", zipCode="12345", country="Country")

# Instantiate Payment
payment1 = Payment(amount=20.0, transactionId="123456", status=PaymentStatus.COMPLETED, paymentMethod=PaymentMethod.CREDIT_CARD)

# Perform actions
seats = [Seat(seatId, payment1.getAmount()) for seatId in range(10)]  # Assuming a new seat for each booking

for j, seat in enumerate(seats):
    booking = Booking(bookingNumber=j, show=show1, seats=[seat], payment=payment1)
    if booking:
        customer1.makeBooking(booking)    
print(f"{customer1.getName()}  Bookings:")
for booking in customer1.getBookings():
    print(f"Booking Number: {booking._bookingNumber}, Status: {booking._status}")

# Cancel a booking
if customer1.getBookings():
    booking_to_cancel = customer1.getBookings()[0]  # Choose the first booking for cancellation
    customer1.cancelBooking(booking_to_cancel)

# Refund a booking
if customer1.getBookings():
    booking_to_refund = booking_to_cancel  # Choose the first booking for refund
    refund_amount = booking_to_refund.refund()
    print(f"Refund Amount for Booking {booking_to_refund._bookingNumber}: {refund_amount}")

available_seats = Seat.get_available_seats(seats)
for seat in available_seats:
    print(seat)
front_desk_assistant.createBookingAndIssueTicket(booking)
theater_administrator.addShow(show1, movie_hall1)
system_administrator.addNewTheaterCompany(theater_administrator)

# Display information (you can add more information based on your classes and methods)
print(f"Customer Name: {customer1.getName()}")
print(f"Front Desk Assistant Name: {front_desk_assistant.getName()}")
print(f"Theater Administrator Name: {theater_administrator.getName()}")
print(f"System Administrator Name: {system_administrator.getName()}")
print(f"Shows in {movie_hall1._name} :-")
for show in movie_hall1.getShows():
    print(show.getShowInfo())
print(f"Shows in {movie_hall2._name} :-")
for show in movie_hall2.getShows():
    print(show.getShowInfo())
# Add more print statements and actions as needed based on your specific class design and methods.
