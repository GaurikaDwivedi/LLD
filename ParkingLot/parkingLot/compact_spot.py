from .parking_spot import ParkingSpot, ParkingSpotType
from .vehicle import Vehicle
class CompactSpot(ParkingSpot):
    def __init__(self, spotNumber, isHandicappedSpot, parkingFloor):
        super().__init__(spotNumber=spotNumber, type=ParkingSpotType.COMPACT, isHandicappedSpot=isHandicappedSpot, parkingFloor=parkingFloor)


    def canPark(self, vehicle):
        return vehicle.getType() != Vehicle.VehicleType.FULLSIZE
