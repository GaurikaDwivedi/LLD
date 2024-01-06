class CarRentalsystem:
    def __init__(self):
        self._name = None
        self._locations = []
        self._vehicles = []  # Add a list to store vehicles

    def addNewLocation(self, location):
        if not location in self._locations:
            self._locations.append(location)
            return True
        return False

    def removeLocation(self, location):
        if not location in self._locations:
            self._locations.remove(location)
            return True
        return False
    
    def addVehicle(self, vehicle):
        if vehicle not in self._vehicles:
            self._vehicles.append(vehicle)
            vehicle.setAvailable(True)               
            return True
        return False

    def removeVehicle(self, vehicle):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)
            vehicle.setAvailable(False)
            return True
        return False
    
    def getAvailableVehicles(self):
        available_vehicles = [vehicle for vehicle in self._vehicles if vehicle.getisAvailable()]
        return available_vehicles