from hotel_management.hotel import Hotel
from hotel_management.hotelLocation import HotelLocation
from hotel_management.room import Room
from hotel_management.notification import Notification
from hotel_management.room_booking import RoomBooking
from hotel_management.invoice import Invoice
from hotel_management.room_housekeeping import RoomHouseKeeping
from hotel_management.room_charge import RoomCharge
from datetime import date

class Tests:

    @classmethod
    def hotel_management_flow(cls):
        my_hotel = Hotel("The Sun Palace")

        # Add some locations to the hotel
        location1 = HotelLocation("Udaipur", "Street 1", 9876543)
        location2 = HotelLocation("Jaipur", "Street 5", 7654321)
        my_hotel.add_location(location1)
        my_hotel.add_location(location2)

        # Get the name and locations of the hotel
        print("Hotel Name:", my_hotel.get_name())
        print("Hotel Locations:")
        locations = my_hotel.get_locations()
        for location in locations:
            print("Location:", location.get_location())
            print("Address:", location.get_address())
            print("Phone Number:", location.get_phone_number())
            print()

        # Create a Room object
        room1 = Room(101, "Deluxe", 2500, availability=True)
        room2 = Room(102, "Deluxe", 2500, availability=True)

        # create a RoomHouseKeeping object

        housekeeping_entry = RoomHouseKeeping(room1, '23-02-2023','Clean')
        housekeeping_entry2 = RoomHouseKeeping(room2, '23-02-2023','Clean')
        
        print("Room Number:", housekeeping_entry.get_room().get_room_number())
        print("Room Style:", housekeeping_entry.get_room().get_room_style())
        print("Date:", housekeeping_entry.get_date())
        print("Status:", housekeeping_entry.get_status())
        RoomHouseKeeping.display_all_entries()

        # Create a RoomBooking object
        today = date.today()
        booking1 = RoomBooking(room1, "Suraj Pandey", 3, today)
        booking1.make_booking()

        # Get the details of the RoomBooking
        print("Guest Name:", booking1.get_guest_name())
        print("Room Number:", booking1.get_room().get_room_number())
        print("Room Style:", booking1.get_room().get_room_style())
        print("Booking Price:", booking1.get_room().get_booking_price())
        print("Booking date", booking1.get_booking_date())
        print("Number of Nights:", booking1.get_number_of_nights())
        print("Checkout date", booking1.get_booking_date())

        RoomHouseKeeping.display_all_entries()
        
        # Create a Notification object
        notification1 = Notification("Your booking has been confirmed.", "Suraj Pandey")
        # Get the details of the Notification
        print("Message:", notification1.get_message())
        print("Recipient:", notification1.get_recipient())
        
        room_charge = RoomCharge(room1,booking1.get_guest_name(), booking1.get_room().get_booking_price())
        invoice = Invoice(room_charge.get_room(), room_charge.get_charge_amount())
        room = invoice.get_room()
        print("Receipt:")
        print("Guest Name:", room_charge.get_charge_name())
        print(f"Booking charge of room {room.get_room_number()} is {invoice.get_charges()} .")

test = Tests()
test.hotel_management_flow()