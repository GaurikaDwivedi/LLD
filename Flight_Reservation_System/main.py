from datetime import datetime, timedelta
from flight_reservation_system.airlineSystem import AirlineSystem
from flight_reservation_system.flight import Flight
from flight_reservation_system.aircraft import Aircraft
from flight_reservation_system.weekly_schedule import WeeklySchedule
from flight_reservation_system.customSchedule import CustomSchedule
from flight_reservation_system.admin import Admin
from flight_reservation_system.address import Address
from flight_reservation_system.airport import Airport
from flight_reservation_system.customer import Customer
from flight_reservation_system.reservation import Reservation
from flight_reservation_system.passenger import Passenger

def main():
    # Create an airline system
    airline_system = AirlineSystem()

    address1 = Address(streetAddress="123 Main St", city="City1", state="State1", zipCode="12345", country="Country1")
    address2 = Address(streetAddress="456 Side St", city="City2", state="State2", zipCode="67890", country="Country2")

    # Create an admin
    admin = Admin(name="Admin Name", address=address1, email="admin@example.com", phone="1234567890")
    admin.airlinesManagementSystem = airline_system

    # Create an aircraft
    aircraft = Aircraft(name="Boeing 747", model="747", manufacturingYear=2020, seats=300)
    aircraft2 = Aircraft(name="Boeing 749", model="749", manufacturingYear=2021, seats=300)

    admin.addAircraft(aircraft)
    admin.addAircraft(aircraft2)

    # Create a flight
    flight1 = Flight(flightNumber="F123", departure="CityA", arrival="CityB", durationInMinutes=120, aircraft=aircraft)
    flight2 = Flight(flightNumber="F456", departure="CityB", arrival="CityC", durationInMinutes=120, aircraft=aircraft2)


    # Add the flight to the airline system
    admin.addFlight(flight1)
    admin.addFlight(flight2)

    # Create a weekly schedule for the flight
    weekly_schedule = WeeklySchedule(daysOfWeek=["MONDAY", "WEDNESDAY"], departureTime="08:00 AM")
    flight1.addNewWeeklySchedule(weekly_schedule)

    # Create a custom schedule for the flight
    custom_schedule = CustomSchedule(customDateTime=datetime.now() + timedelta(days=7))
    custom_schedule.setDay(day=["TUESDAY"],)
    flight2.addNewCustomSchedule(custom_schedule)
    
    # Display Available Flights
    print("\nAvailable Flights in My Airline:")
    available_flights_for_airline = airline_system.getAvailableFlights()
    for flight in available_flights_for_airline:
        print(f"Flight Number: {flight.getFlightNumber()}, WeeklySchedules:{[(schedule.getDaysOfWeek(), schedule.getDepartureTime()) for schedule in flight.getWeeklySchedules()]}, CustomSchedules:{[(schedule.getDay(), schedule.getCustomDateTime()) for schedule in flight.getCustomSchedules()]}")

    # Create an airport
    airport = Airport(name="CityA Airport", address=address1, code="CA")

    # Add the flight to the airport
    airport.addNewFlight(flight1)

    #Flights in particular airport
    available_flights_for_airport = airport.getFlights()
    print(f"\nAvailable Flights in {airport.getName()}:")
    for flight in available_flights_for_airport:
        print(f"Flight Number: {flight.getFlightNumber()}, WeeklySchedules:{[(schedule.getDaysOfWeek(), schedule.getDepartureTime()) for schedule in flight.getWeeklySchedules()]}, CustomSchedules:{[(schedule.getDay(), schedule.getCustomDateTime()) for schedule in flight.getCustomSchedules()]}")


    # Create a customer
    customer1 = Customer(name="John Doe", address=address1, email="john@example.com", phone="9876543210", frequentFlyerNumber="FF123")
    customer2 = Customer(name="Chritian", address=address2, email="christian@example.com", phone="9891243210", frequentFlyerNumber="FF125")
    # Create a reservation for the customer
    reservation1 = Reservation(
        confirmationNumber="R123",
        primaryTraveller=customer1,
        flights=[flight1],
        seats=["A1"],
        passengers=[Passenger(name="Passenger Name", dateOfBirth="2000-01-01", passportNumber="AB123456")]
    )
    reservation2 = Reservation(
        confirmationNumber="R124",
        primaryTraveller=customer2,
        flights=[flight2],
        seats=["C1"],
        passengers=[Passenger(name="Passenger Name", dateOfBirth="2000-01-01", passportNumber="AB123456")]
    )

    # Make a reservation and get the itinerary
    itinerary = customer1.makeReservationAndGetItinerary(reservation1, transactionId="123")
    
    # Display the itinerary
    print(f"Itinerary of {customer1.getName()}:")
    print(f"Confirmation Number: {itinerary.getConfirmationNumber()}")
    print(f"Primary Traveller: {itinerary.getPrimaryTraveller().getName()}")
    print(f"Flight: {[f.getFlightNumber() for f in itinerary.getFlights()]}")
    print(f"Seat: {itinerary.getSeats()}")
    print(f"Creation Date Time: {itinerary.getCreationDateTime()}")

    itinerary_customer2 = customer2.makeReservationAndGetItinerary(reservation2, transactionId="567")
    print(f"Itinerary of {customer2.getName()}:")
    print(f"Confirmation Number: {itinerary_customer2.getConfirmationNumber()}")
    print(f"Primary Traveller: {itinerary_customer2.getPrimaryTraveller().getName()}")
    print(f"Flight: {[f.getFlightNumber() for f in itinerary_customer2.getFlights()]}")
    print(f"Seat: {itinerary_customer2.getSeats()}")
    print(f"Creation Date Time: {itinerary_customer2.getCreationDateTime()}")

    message = customer2.cancelReservation(reservation2)
    print(message)

if __name__ == "__main__":
    main()
