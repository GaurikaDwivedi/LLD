class HotelLocation:
    def __init__(self, location, address, phoneNumber):
        self.location = location
        self.address = address
        self.phoneNumber = phoneNumber

    def get_location(self):
        return self.location

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phoneNumber
