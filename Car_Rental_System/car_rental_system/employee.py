from car_rental_system.user import User
class Employee(User):
    def __init__(self, employeeId, name, email, phone):
        super().__init__(name, email, phone)
        self.employeeId = employeeId

    def getEmployeeId(self):
        return self.employeeId

    def updateEmployeeId(self, employeeId):
        self.employeeId = employeeId