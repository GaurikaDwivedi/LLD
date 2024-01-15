import time
from enum import Enum
from amazon.notification import Notification
from amazon.shipmentStatus import ShipmentStatus
class OrderStatus(Enum):
    PENDING = 0
    PLACED = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4
    REFUND_APPLIED = 5

class Order:
    def __init__(self, orderNumber, productsOrdered):
        self._orderNumber = orderNumber
        self._status = OrderStatus.PENDING
        self._orderDate = round(time.time() * 1000)
        self._productsOrdered = productsOrdered
        self._associatedPaymentDetail = None
        self._shipmentDetail = None

    def ship(self, shipmentDetail):
        self._status = OrderStatus.SHIPPED
        self.updateShipmentDetail(shipmentDetail)
        notification = Notification(f"Order Status: {self.getStatus().name}.\n"
                                    f"Shipping Details:\n"
                                    f"Shipping Number: {self.getShipmentDetail().getShipmentNumber()}.\n"
                                    f"Shipping Date: {self.getShipmentDetail().getShipmentDate()}.\n"
                                    f"Estimated Arrival: {self.getShipmentDetail().getEstimatedArrival()}.\n")
        notification.send()

    def deliver(self):
        if self.getStatus() == OrderStatus.SHIPPED:
            self.updateStatus(OrderStatus.DELIVERED)
            if self.getShipmentDetail():
                self.getShipmentDetail().updateStatus(ShipmentStatus.DELIVERED)

            notification = Notification(f"Order Delivered. Order Status: {self.getStatus().name}.\n"
                                        f"Order Number: {self.getOrderNumber()}.\n"
                                        f"Products Delivered: {[product.getName() for product in self.getProductsOrdered()]}\n")
            notification.send()

    def cancel(self):
        if self.getStatus() == OrderStatus.PENDING or self.getStatus() == OrderStatus.PLACED:
            self.updateStatus(OrderStatus.CANCELED)
            if self.getShipmentDetail():
                self.getShipmentDetail().updateStatus(ShipmentStatus.CANCELED)

            notification = Notification(f"Order Canceled. Order Status: {self.getStatus().name}.\n"
                                        f"Order Number: {self.getOrderNumber()}.\n"
                                        f"Products Canceled: {[product.getName() for product in self.getProductsOrdered()]}\n")
            notification.send()
        
        elif (self.getStatus() == OrderStatus.DELIVERED):
            notification = Notification(f"Cancel request not allowed for the {self.getStatus().name} order. Place return request.")
            notification.send()

        else:
            notification = Notification(f"Return request not allowed for the current order status.")
            notification.send()

    def returnOrder(self):
        if self.getStatus() == OrderStatus.DELIVERED:
            if self.getShipmentDetail():
                self.getShipmentDetail().updateStatus(ShipmentStatus.RETURN_REQUESTED)
            notification = Notification(f"Return Requested. Order Status: {self.getStatus().name}.\n"
                                        f"Order Number: {self.getOrderNumber()}.\n"
                                        f"Products to Return: {[product.getName() for product in self.getProductsOrdered()]}\n")
            notification.send()
            self.refund()
        else:
            notification = Notification(f"Return request not allowed for the current order status.")
            notification.send()


    def updateShipmentDetail(self, shipmentDetail):
        self._shipmentDetail = shipmentDetail

    def getShipmentDetail(self):
        return self._shipmentDetail

    def refund(self):
        refund_amount = self.calculateTotal()
        if self._associatedPaymentDetail:
                self._associatedPaymentDetail.refund(refund_amount)
                self.updateStatus(OrderStatus.REFUND_APPLIED)

    def updateStatus(self, status):
        self._status = status

    def makePayment(self, payment):
        self._associatedPaymentDetail = payment
        self.updateStatus(OrderStatus.PLACED)
        notification = Notification(f"Payment Successful. Order Status: {self.getStatus().name}.\n"
                                    f"Order Details:\n"
                                    f"Order Number: {self.getOrderNumber()}.\n"
                                    f"Products Ordered: {[product.getName() for product in self.getProductsOrdered()]}\n")
        notification.send()
        
    def getOrderNumber(self):
        return self._orderNumber

    def getStatus(self):
        return self._status

    def getOrderDate(self):
        return self._orderDate

    def getProductsOrdered(self):
        return self._productsOrdered
    
    def calculateTotal(self):
        total = 0
        for product in self._productsOrdered:
            total += product.getPrice()
        return total

