from .parking_spot import ParkingSpotType
from .vehicle import VehicleType
class ParkingFloor:
    def __init__(self, floorId):
        self._floorId = floorId
        self._availableCompactSpots_nonADA = []
        self._availableLargeSpots_nonADA = []
        self._availableMotorcycleSpots_nonADA = []
        self._availableElectricSpots_nonADA = []
        self._availableCompactSpots_handicapped = []
        self._availableLargeSpots_handicapped = []
        self._availableMotorcycleSpots_handicapped = []
        self._availableElectricSpots_handicapped = []

    def updateFloorId(self,floorId):
        self._floorId = floorId
    
    def getFloorID(self):
        return self._floorId
    
    def printAllParkingSpots(self, spots, spotType):
        if spots:
            print(f"{spotType} Slots:")
            for spot in spots:
                print(f" - Spot Number: {spot.getSpotNumber()}, Type: {spot.getType().name}, Available: {spot.getIsAvailable()}")
        else:
            print(f"No {spotType} Slots.")
    
    def getAllParkingSpots(self):
        self.printAllParkingSpots(self._availableCompactSpots_nonADA, "NonADA Compact")
        self.printAllParkingSpots(self._availableLargeSpots_nonADA, "NonADA Large")
        self.printAllParkingSpots(self._availableMotorcycleSpots_nonADA, "NonADA Motorcycle")
        self.printAllParkingSpots(self._availableElectricSpots_nonADA, "NonADA Electric")
        self.printAllParkingSpots(self._availableCompactSpots_handicapped, "Handicapped Compact")
        self.printAllParkingSpots(self._availableLargeSpots_handicapped, "Handicapped Large")
        self.printAllParkingSpots(self._availableMotorcycleSpots_handicapped, "Handicapped Motorcycle")
        self.printAllParkingSpots(self._availableElectricSpots_handicapped, "Handicapped Electric")

    def addParkingSpot(self, spot):
        spotType = spot.getType()
        if spotType is ParkingSpotType.MOTORCYCLE:
            if spot.getIsHandicappedSpot():
                self._availableMotorcycleSpots_handicapped.append(spot)
            else:
                self._availableMotorcycleSpots_nonADA.append(spot)
        elif spotType is ParkingSpotType.COMPACT:
            if spot.getIsHandicappedSpot():
                self._availableCompactSpots_handicapped.append(spot)
            else:
                self._availableCompactSpots_nonADA.append(spot)
        elif spotType is ParkingSpotType.LARGE:
            if spot.getIsHandicappedSpot():
                self._availableLargeSpots_handicapped.append(spot)
            else:
                self._availableLargeSpots_nonADA.append(spot)
        elif spotType is ParkingSpotType.ELECTRIC:
            if spot.getIsHandicappedSpot():
                self._availableElectricSpots_handicapped.append(spot)
            else:
                self._availableElectricSpots_nonADA.append(spot)
        else:
            raise Exception("Wrong input")
        spot.setParkingFloor(self)

    def parkVehicle(self, vehicle):
        if self.isFull1():
            print("Floor is full, no spots available.")
        spot_to_park = None

        if vehicle.getType() == VehicleType.MOTORCYCLE:
            if self._availableMotorcycleSpots_nonADA:
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableMotorcycleSpots_nonADA,
                                                    self._availableMotorcycleSpots_handicapped)
            elif self._availableCompactSpots_nonADA:  # Check for available compact spots if motorcycle spots are not available
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableCompactSpots_nonADA,
                                                    self._availableCompactSpots_handicapped)
        elif vehicle.getType() == VehicleType.COMPACT:
            if self._availableCompactSpots_nonADA:
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableCompactSpots_nonADA,
                                                self._availableCompactSpots_handicapped)
            elif self._availableLargeSpots_nonADA: # Check for available large spots if compact spots are not available
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableLargeSpots_nonADA,
                                                self._availableLargeSpots_handicapped)
        elif vehicle.getType() == VehicleType.LARGE:
            if self._availableLargeSpots_nonADA:
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableLargeSpots_nonADA,
                                                self._availableLargeSpots_handicapped)
            elif self._availableElectricSpots_nonADA:
                spot_to_park = self._parkVehicleHelper(vehicle, self._availableElectricSpots_nonADA,
                                                self._availableElectricSpots_handicapped)
        elif vehicle.getType() == VehicleType.ELECTRIC:
            spot_to_park = self._parkVehicleHelper(vehicle, self._availableElectricSpots_nonADA,
                                                self._availableElectricSpots_handicapped)
        else:
            raise print("Invalid vehicle type")

        if spot_to_park:
            print(f"{vehicle.getLicenseNumber()} is parked at spot {spot_to_park.getSpotNumber()}")
            spot_to_park.assignVehicle(vehicle)


    def _parkVehicleHelper(self, vehicle, nonAdaParkingSpots, adaParkingSpots):
        if vehicle.getisHandicapped():
            if not adaParkingSpots:
                print(f"No handicapped parking spot is available for your vehicle type i.e. {vehicle.getType().name}")
            else:
                return adaParkingSpots.pop(0)
        else:
            if not nonAdaParkingSpots:
                print("No non-ADA parking spot is available for your vehicle type.")
            else:
                return nonAdaParkingSpots.pop(0)

    def freeSpot(self, spot):
        spot.removeVehicle()
        type = spot.getType()
        if type == ParkingSpotType.MOTORCYCLE:
            if spot.getIsHandicappedSpot():
                self._availableMotorcycleSpots_handicapped.append(spot)
            else:
                self._availableMotorcycleSpots_nonADA.append(spot)
        elif type == ParkingSpotType.COMPACT:
            if spot.getIsHandicappedSpot():
                self._availableCompactSpots_handicapped.append(spot)
            else:
                self._availableCompactSpots_nonADA.append(spot)
        elif type == ParkingSpotType.LARGE:
            if spot.getIsHandicappedSpot():
                self._availableLargeSpots_handicapped.append(spot)
            else:
                self._availableLargeSpots_nonADA.append(spot)
        elif type == ParkingSpotType.ELECTRIC:
            if spot.getIsHandicappedSpot():
                self._availableElectricSpots_handicapped.append(spot)
            else:
                self._availableElectricSpots_nonADA.append(spot)

    def isFull1(self):
        return len(self._availableCompactSpots_handicapped) == 0 and len(self._availableMotorcycleSpots_nonADA) == 0 and len(self._availableMotorcycleSpots_handicapped) == 0 and len(self._availableCompactSpots_handicapped) == 0 and len(self._availableCompactSpots_nonADA) == 0 and len(self._availableElectricSpots_handicapped) == 0 and len(self._availableLargeSpots_handicapped) == 0 and len(self._availableLargeSpots_nonADA) == 0

    def isFull(self, vehicle):
        if vehicle.getType() == VehicleType.MOTORCYCLE:
            if vehicle.getisHandicapped():
                return len(self._availableMotorcycleSpots_handicapped) == 0
            return len(self._availableMotorcycleSpots_nonADA) == 0
        if (vehicle.getType() == VehicleType.MOTORCYCLE) or (vehicle.getType() == VehicleType.COMPACT):
            if vehicle.getisHandicapped():
                return len(self._availableCompactSpots_handicapped) == 0
            return len(self._availableCompactSpots_nonADA) == 0
        if (vehicle.getType() == VehicleType.MOTORCYCLE) or (vehicle.getType() == VehicleType.COMPACT) or (vehicle.getType() == VehicleType.FULLSIZE):
            if vehicle.getisHandicapped():
                return len(self._availableLargeSpots_handicapped) == 0
            return len(self._availableLargeSpots_nonADA) == 0
        if (vehicle.getType() == VehicleType.MOTORCYCLE) or (vehicle.getType() == VehicleType.COMPACT) or (vehicle.getType() == VehicleType.FULLSIZE) or (
                vehicle.getType() == VehicleType.ELECTRIC):
            if vehicle.getisHandicapped():
                return len(self._availableElectricSpots_handicapped) == 0
            return len(self._availableElectricSpots_nonADA) == 0

        if True:
            raise Exception("Wrong input")
        
    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != ParkingFloor:
            return False
        that = o
        return self._floorId is that._floorId

    def hashCode(self):
        return hash(self._floorId)