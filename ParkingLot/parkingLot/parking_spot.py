from enum import Enum

class ParkingSpotType(Enum):
    COMPACT = 0
    LARGE = 1
    MOTORCYCLE = 2
    ELECTRIC = 3
class ParkingSpot:

    def _initialize_instance_fields(self):
        self._spotNumber = None
        self._isAvailable = True
        self._vehicleParked = None
        self._type = 0
        self._isHandicappedSpot = False
        self._parkingFloor = None

    def __init__(self, spotNumber, type, isHandicappedSpot, parkingFloor):
        self._initialize_instance_fields()
        self._spotNumber = spotNumber
        self._type = type
        self._isHandicappedSpot = isHandicappedSpot
        self._parkingFloor = parkingFloor

    def canPark(self, vehicle):
        pass

    def assignVehicle(self, vehicle):
        self._vehicleParked = vehicle
        self._isAvailable = False

    def removeVehicle(self):
        self._vehicleParked = None
        self._isAvailable = True
    
    def getSpotNumber(self):
        return self._spotNumber
    
    def setIsAvailable(self,available):
        self._isAvailable =  available

    def getIsAvailable(self):
        return self._isAvailable

    def getVehicleParked(self):
        return self._vehicleParked

    def getType(self):
        return self._type

    def getIsHandicappedSpot(self):
        return self._isHandicappedSpot

    def getParkingFloor(self):
        return self._parkingFloor

    def setParkingFloor(self, parkingFloor):
        self._parkingFloor = parkingFloor

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != ParkingSpot:
            return False
        that = o
        if self._isHandicappedSpot != that._isHandicappedSpot:
            return False
        if self._spotNumber != that._spotNumber:
            return False
        if self._type != that._type:
            return False
        return self._parkingFloor is that._parkingFloor

    def hashCode(self):
        result = hash(self._spotNumber)
        result = 31 * result + hash(self._type)
        result = 31 * result + (1 if self._isHandicappedSpot else 0)
        return result
