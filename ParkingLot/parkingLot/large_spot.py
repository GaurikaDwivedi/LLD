from .parking_spot import ParkingSpot, ParkingSpotType
class LargeSpot(ParkingSpot):
    def __init__(self, spotNumber, isHandicappedSpot, parkingFloor):
        super().__init__(spotNumber=spotNumber, type=ParkingSpotType.LARGE, isHandicappedSpot=isHandicappedSpot, parkingFloor=parkingFloor)


    def canPark(self, vehicle):
        return True