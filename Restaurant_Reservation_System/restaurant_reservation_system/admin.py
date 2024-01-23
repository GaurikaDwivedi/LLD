from restaurant_reservation_system.employee import Employee
class SystemAdmin(Employee):
    def __init__(self, name, email, phone, employeeID, dateJoined):
        self._system = None
        super().__init__(name, email, phone, employeeID, dateJoined)

    def addNewClient(self, restaurant):
        self._system.addNewClient(restaurant)

    def removeClient(self, restaurant):
        self._system.removeClient(restaurant)