from restaurant_reservation_system.employee import Employee
class Manager(Employee):
    def __init__(self, name, email, phone, employeeID, dateJoined):
        super().__init__(name, email, phone, employeeID, dateJoined)

    def addEmployee(self, emp):
        pass