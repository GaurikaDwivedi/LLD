from datetime import timedelta
from hotel_management.room_housekeeping import RoomHouseKeeping

class RoomBooking:
    def __init__(self, room, guest_name, number_of_nights, booking_date):
        self.room = room
        self.guest_name = guest_name
        self.number_of_nights = number_of_nights
        self.booking_date = booking_date

    def get_room(self):
        return self.room

    def get_guest_name(self):
        return self.guest_name

    def get_number_of_nights(self):
        return self.number_of_nights
    
    def get_booking_date(self):
        return self.booking_date
    
    def checkout_date(self):
        checkout_date = self.booking_date + timedelta(days=self.number_of_nights)
        return checkout_date

    def make_booking(self):
        # Check room availability and status before making a booking
        if self.room.is_available():
            room_status = self.get_room_status(self.room)
            if room_status == "Clean":
                if self.room.book_room():
                    # Update housekeeping status to "Booked"
                    self.update_housekeeping_status(self.room, self.get_booking_date(), "Booked")
                    print(f"Booking for Room {self.room.get_room_number()} is successful.")
                else:
                    print(f"Room {self.room.get_room_number()} could not be booked.")
            else:
                print(f"Room {self.room.get_room_number()} is not available for booking due to status: {room_status}.")
        else:
            print(f"Room {self.room.get_room_number()} is not available for booking.")


    def get_room_status(self,room):
        # Find the latest status entry for the specified room
        status_entries = [entry for entry in RoomHouseKeeping.all_entries if entry.get_room() == room]
        if status_entries:
            latest_entry = max(status_entries, key=lambda entry: entry.get_date())
            return latest_entry.get_status()
        else:
            return "Unknown"
        
    def update_housekeeping_status(self, room, date, status):
        # Find and update the status of an existing housekeeping entry
        for entry in RoomHouseKeeping.all_entries:
            if entry.get_room() == room:
                entry.status = status
                print(f"Housekeeping status updated for Room {room.get_room_number()} on {date}.")
                return
        print("Housekeeping entry not found.")


