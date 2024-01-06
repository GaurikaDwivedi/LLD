from employee import Employee
class CustomerAssistant(Employee):
    def __init__(self, employeeId, name, email, phone):
        super().__init__(employeeId, name, email, phone)

    def searchMember(self, query):
        pass

    def makeReservation(self, customer, reservation):
        customer.completeReservation(reservation)