from .vehicle import Vehicle, VehicleType

class Motorcycle(Vehicle):
    def __init__(self, licenseNumber, isHandicapped):
        super().__init__(licenseNumber, isHandicapped)
        self.type = VehicleType.MOTORCYCLE
