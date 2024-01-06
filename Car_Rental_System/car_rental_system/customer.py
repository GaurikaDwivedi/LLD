from car_rental_system.user import User
from car_rental_system.carType import EconomyCar
class Customer(User):
    def __init__(self, driverLicense, name, email, phone):
        super().__init__(name, email, phone)
        self._license = driverLicense
        self._reservationHistory = []
        self._search = None

    def mostRecentReservation(self):
        return self._reservationHistory[len(self._reservationHistory) - 1]

    def completeReservation(self, reservation):
        self._reservationHistory.append(reservation)

    def searchVehicle(self, available_vehicles, query, vehiclePickupDateTime, vehicleDropOffDateTime):
        matching_vehicles = []
        for vehicle in available_vehicles:
            if query.lower() in vehicle.getModel().lower() or query.lower() in vehicle.getMake().lower():
                if vehicle.getisAvailable():
                    matching_vehicles.append(vehicle)
        return matching_vehicles