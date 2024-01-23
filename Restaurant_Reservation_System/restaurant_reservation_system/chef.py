from restaurant_reservation_system.employee import Employee
from restaurant_reservation_system.table_order import OrderStatus
from restaurant_reservation_system.notification import Notification
class Chef(Employee):
    def __init__(self, name, email, phone, employeeID, dateJoined):
        super().__init__(name, email, phone, employeeID, dateJoined)

    def prepareOrder(self, order):
        notification = Notification(f"Chef {self.getName()} is preparing the order.")
        notification.send()
        # Simulate order preparation process
        order.updateStatus(OrderStatus.PREPARING)
        order.updateStatus(OrderStatus.COMPLETED)
        notification = Notification(f"Chef {self.getName()} has completed preparing the order.")
        notification.send()
