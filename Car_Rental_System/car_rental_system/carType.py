from .vehicle import Vehicle, CarType
class EconomyCar(Vehicle):
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        super().__init__(licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear)
        self.carType = CarType.ECONOMY

class PickupTruck(Vehicle):
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        super().__init__(licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear)
        self.carType = CarType.TRUCK

class ElectricCar(Vehicle):
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        super().__init__(licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear)
        self.carType = CarType.ELECTRIC

class CompactCar(Vehicle):
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        super().__init__(licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear)
        self.carType = CarType.COMPACT
        
class FullsizeCar(Vehicle):
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        super().__init__(licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear)
        self.carType = CarType.FULL_SIZE