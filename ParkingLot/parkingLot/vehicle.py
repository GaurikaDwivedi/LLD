from enum import Enum
class VehicleType(Enum):
        COMPACT = 0
        LARGE = 1
        ELECTRIC = 3
        MOTORCYCLE = 2

class Vehicle:
    
    def __init__(self, licenseNumber, isHandicapped):
        self.type = 0
        self.ticket = None
        self.licenseNumber = licenseNumber
        self.isHandicapped = isHandicapped

    def assignTicket(self, ticket):
        self.ticket = ticket

    def getLicenseNumber(self):
        return self.licenseNumber

    def getType(self):
        return self.type

    def getTicket(self):
        return self.ticket

    def getisHandicapped(self):
        return self.isHandicapped

    def setHandicapped(self, handicapped):
        self.isHandicapped = handicapped