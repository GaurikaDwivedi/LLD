from restaurant_reservation_system.employee import Employee
from restaurant_reservation_system.table_order import OrderStatus
from restaurant_reservation_system.notification import Notification

class Waiter(Employee):
    def __init__(self, name, email, phone, employeeID, dateJoined):
        super().__init__(name, email, phone, employeeID, dateJoined)
    
    def takeOrder(self, tableOrder):
        if tableOrder and tableOrder.getStatus() == OrderStatus.RECEIVED:
            # Logic for taking the order, updating status, etc.
            tableOrder.updateStatus(OrderStatus.PREPARING)
            notification = Notification(
                message=f"Waiter {self.getName()} has taken the order for Table {tableOrder.getTable().getTableID()}."
            )    
        else:
            notification = Notification(message=f"Invalid order status or table order not provided.")
        notification.send()

    def serveOrder(self, tableOrder):
        if tableOrder and tableOrder.getStatus() == OrderStatus.COMPLETED:
            # Logic for serving the order, updating status, etc.
            tableOrder.updateStatus(OrderStatus.SERVED)
            notification = Notification(f"Waiter {self.getName()} has served the order to Table {tableOrder.getTable().getTableID()}.")
        else:
            notification = Notification(f"Invalid order status or table order not provided.")
        notification.send()


   