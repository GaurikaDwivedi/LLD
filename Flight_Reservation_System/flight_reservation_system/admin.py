from flight_reservation_system.user import User
class Admin(User):
    def __init__(self, name, address, email, phone):
        self.airlinesManagementSystem = None
        super().__init__(name, address, email, phone)

    def addAircraft(self, aircraft):
        return self.airlinesManagementSystem.addAircraft(aircraft)

    def removeAircraft(self, aircraft):
        return self.airlinesManagementSystem.removeAircraft(aircraft)

    def addFlight(self, flight):
        return self.airlinesManagementSystem.addFlight(flight)

    def removeFlight(self, flight):
        return self.airlinesManagementSystem.removeFlight(flight)

    def addNewFlightInstance(self, specificFlightInstance):
        return self.airlinesManagementSystem.addSpecificFlightInstance(specificFlightInstance)

    def cancelFlightInstance(self, specificFlightInstance):
        return self.airlinesManagementSystem.removeSpecificFlightInstance(specificFlightInstance)