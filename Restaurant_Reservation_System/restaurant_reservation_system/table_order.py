from enum import Enum
class OrderStatus(Enum):
        RECEIVED = 0
        PREPARING = 1
        COMPLETED = 2
        CANCELED = 3
        SERVED = 4

class TableOrder:
    def __init__(self, table):
        self._OrderID = 0
        self._status = 0
        self._orders = []
        self._table = table
        
    def setOrderIDAutoIncrement(self):
        self._OrderID+=1
    
    def getOrderID(self):
        return self._OrderID
    
    def addOrder(self, order):
        self._orders.append(order)
        self.setOrderIDAutoIncrement()

    def removeOrder(self, order):
        self._orders.remove(order)

    def getStatus(self):
        return self._status

    def updateStatus(self, status):
        self._status = status

    def getTable(self):
        return self._table
    
    def calculateTotalAmount(self):
        total_amount = 0
        for order in self._orders:
            total_amount += order.getPrice()
        return total_amount
