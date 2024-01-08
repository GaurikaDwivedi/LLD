from .vehicle import Vehicle, VehicleType
class ElectricCar(Vehicle):
    def __init__(self, licenseNumber, isHandicapped):
        super().__init__(licenseNumber, isHandicapped)
        self.type = VehicleType.ELECTRIC