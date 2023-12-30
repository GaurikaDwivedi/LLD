class Room:
    def __init__(self, room_number, room_style, booking_price,availability):
        self.room_number = room_number
        self.room_style = room_style
        self.booking_price = booking_price
        self.availability = availability

    def get_room_number(self):
        return self.room_number

    def get_room_style(self):
        return self.room_style

    def get_booking_price(self):
        return self.booking_price
    
    def is_available(self):
        return self.availability

    def book_room(self):
        if self.availability:
            self.availability = False
            return True
        else:
            return False