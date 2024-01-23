from restaurant_reservation_system.notification import Notification
from restaurant_reservation_system.table_order import OrderStatus
from restaurant_reservation_system.payment import Payment, PaymentStatus
from restaurant_reservation_system.reservation import ReservationStatus
import uuid

class Customer:
    def __init__(self, phoneNumber, email, name):
        self._phoneNumber = phoneNumber
        self._email = email
        self._name = name
        self._reservationAmount = 0

    def makeReservation(self, reservation, branch, table, reservingTableCharge):
        if branch.reserveTableForReservation(reservation, table):
            self._reservationAmount += reservingTableCharge
            notification = Notification(f"Table {table.getTableID()} is {table.getStatus().name} by {self.getName()}. Deposited Amount {self._reservationAmount}")
        else:
            notification = Notification(f"Table {table.getTableID()} is already {table.getStatus().name}. Try reserving another table.")
        notification.send()

    def cancelReservation(self, reservation, branch, table):
        if reservation.cancelReservation():
            payment = Payment(transactionId=self.generate_transaction_id())
            payment.refund()
            notification = Notification(f"Reservation canceled successfully. Refunded amount {self._reservationAmount}")
            branch.freeTableForReservation(reservation, table)
        else:
            notification = Notification("Cannot cancel reservation. Check status.")
        notification.send()

    def makeTableOrder(self, branch, table, meal):
        reservation = table.getCurrentReservation()
        order = None
        if reservation and reservation.getStatus() == ReservationStatus.RESERVED:
            branch.checkInReservation(reservation, table)
            waiter = self.callWaiter(branch)
            if waiter:
                order = branch.takeTableOrder(table, meal)
                if order:
                    waiter.takeOrder(order)
                    chef = self.getChef(branch)
                    chef.prepareOrder(order)
                    waiter.serveOrder(order)
                    notification = Notification(f"Order {order.getStatus().name} successfully for Table {table.getTableID()}. ")
                else:
                    notification = Notification("Sorry!! Couldn't make order.")
            else:
                notification = Notification("No waiter available. Please wait..")
        else:
            notification = Notification(f"Sorry!! Couldn't make order without prior reservation.")
        notification.send()
        return order
    
    def callWaiter(self, branch):
        waiters = branch.getWaiters()
        if waiters:
            return waiters[0]
        else:
            return None
        
    def getChef(self, branch):
        chefs = branch.getChefs()
        if chefs:
            return chefs[0]
        else:
            notification = Notification("No Chef available. Please wait..")
            notification.send()
            return None

    def generate_transaction_id(self):
        return "TXN" + str(uuid.uuid4().hex)[:8]
    
    def makePayment(self, order):
        if order and order.getStatus() == OrderStatus.SERVED:
            # Create a payment object
            remainingAmount = order.calculateTotalAmount() - self._reservationAmount
            payment = Payment(transactionId=self.generate_transaction_id())
            payment.simulatePayment()
            payment_status = payment.getPaymentStatus()
            if payment_status == PaymentStatus.COMPLETED:
                self._reservationAmount = 0
                notification = Notification(f"Payment of {remainingAmount} successful for Table {order.getTable().getTableID()}, Order {order.getOrderID()}.")
            else:
                notification = Notification(f"Payment failed for Order {order.getOrderID()}. Please try again.")
        else:
            notification = Notification("Invalid order status or order not provided.")
        notification.send()

    def getPhoneNumber(self):
        return self._phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name