from enum import Enum


class CarType(Enum):
    ECONOMY = 0
    COMPACT = 1
    FULL_SIZE = 2
    PREMIUM = 3
    TRUCK = 4
    ELECTRIC = 5

class Vehicle:
    def __init__(self, licensePlateNumber, vin, passengerCapacity, model, make, color, manufacturingYear):
        self.mileage = 0
        self.carType = 0
        self.reservationHistory = None
        self.isAvailable = False

        self.licensePlateNumber = licensePlateNumber
        self.passengerCapacity = passengerCapacity
        self.vin = vin
        self.model = model
        self.make = make
        self.color = color
        self.manufacturingYear = manufacturingYear

    def reserveVehicle(self, reservation):
        if self.isAvailable:
            self.isAvailable = False
            self.reservationHistory.append(reservation)
            return True
        return False

    def returnVehicle(self):
        self.isAvailable = True

    def getLicenseNumber(self):
        return self.licensePlateNumber

    def updateLicenseNumber(self, licensePlateNumber):
        self.licensePlateNumber = licensePlateNumber

    def getPassengerCapacity(self):
        return self.passengerCapacity

    def updatePassengerCapacity(self, passengerCapacity):
        self.passengerCapacity = passengerCapacity

    def getVin(self):
        return self.vin

    def rectifyVin(self, vin):
        self.vin = vin

    def getModel(self):
        return self.model

    def rectifyModel(self, model):
        self.model = model

    def getMake(self):
        return self.make

    def rectifyMake(self, make):
        self.make = make

    def getColor(self):
        return self.color
    
    def supdateColor(self, color):
        self.color = color

    def getManufacturingYear(self):
        return self.manufacturingYear

    def rectifyManufacturingYear(self, manufacturingYear):
        self.manufacturingYear = manufacturingYear

    def getMileage(self):
        return self.mileage

    def updateMileage(self, mileage):
        self.mileage = mileage

    def getCarType(self):
        return self.carType

    def changeCarType(self, carType):
        self.carType = carType

    def getReservationHistory(self):
        return self.reservationHistory

    def addToReservationHistory(self, reservation):
        self.reservationHistory.append(reservation)

    def getisAvailable(self):
        return self.isAvailable

    def setAvailable(self, available):
        self.isAvailable = available