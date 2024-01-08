from .vehicle import Vehicle, VehicleType
class CompactCar(Vehicle):
    def __init__(self, licenseNumber, isHandicapped):
        super().__init__(licenseNumber, isHandicapped)
        self.type = VehicleType.COMPACT

