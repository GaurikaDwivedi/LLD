from restaurant_reservation_system.employee import Employee

class Receptionist(Employee):
    def __init__(self, name, email, phone, employeeID, dateJoined):
        super().__init__(name, email, phone, employeeID, dateJoined)

    def createReservation(self, reservation, customer, branch1, table1, reservingTableCharge):
        customer.makeReservation(reservation, branch1, table1, reservingTableCharge )

    def cancelReservation(self, reservation, customer, branch1, table1):
        customer.cancelReservation(reservation, branch1, table1)

    def searchCustomerByName(self, name):
         # In a real system, you would query a database 
        pass

    def searchCustomerByEmail(self, email):
         # In a real system, you would query a database 
        pass

    def searchCustomerByPhone(self, phone):
         # In a real system, you would query a database 
        pass