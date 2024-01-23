from restaurant_reservation_system.table import TableStatus
from restaurant_reservation_system.table_order import OrderStatus, TableOrder 
from restaurant_reservation_system.notification import Notification
from restaurant_reservation_system.reservation import ReservationStatus
class Branch:
    def __init__(self, branchId, name, location):
        self._branchId = None
        self._name = None
        self._location = None
        self._menu = None
        self._manager = None
        self._chefs = []
        self._waiters = []
        self._receptionists = []
        self._reservationHistory = []

        self._branchId = branchId
        self._name = name
        self._location = location

    def getBranchId(self):
        return self._branchId

    def setBranchId(self, branchId):
        self._branchId = branchId

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
    
    def getLocation(self):
        return self._location

    def setLocation(self, location):
        self._location = location

    def getMenu(self):
        return self._menu

    def setMenu(self, menu):
        self._menu = menu

    def addManager(self, manager):
        self._manager = manager

    def getManager(self):
        return self._manager

    def changeManager(self, manager):
        self._manager = manager

    def getChefs(self):
        return self._chefs

    def addChef(self, chef):
        if not chef in self._chefs:
            self._chefs.append(chef)

    def removeChef(self, chef):
        if chef in self._chefs:
            self._chefs.remove(chef)

    def getWaiters(self):
        return self._waiters
    
    def addWaiter(self, waiter):
        if not waiter in self._waiters:
            self._waiters.append(waiter)

    def removeWaiter(self, waiter):
        if waiter in self._waiters:
            self._waiters.remove(waiter)

    def getReceptionists(self):
        return self._receptionists

    def addReceptionist(self, receptionist):
        if not receptionist in self._receptionists:
            self._receptionists.append(receptionist)

    def removeReceptionist(self, receptionist):
        if receptionist in self._receptionists:
            self._receptionists.remove(receptionist)
    
    def getReservationHistory(self):
        return self._reservationHistory

    def addReservation(self, reservation):
        if not reservation in self._reservationHistory:
            self._reservationHistory.append(reservation)

    def removeReservation(self, reservation):
        if reservation in self._reservationHistory:
            self._reservationHistory.remove(reservation)

    def reserveTableForReservation(self, reservation, table):
        if table.checkIsTableAvailable():
            table.setCurrentReservation(reservation)
            table.setStatus(TableStatus.RESERVED)
            reservation.updateStatus(ReservationStatus.RESERVED)
            self.addReservation(reservation)
        else:
            return False
        return True
    
    def checkInReservation(self, reservation, table):
        if reservation in self._reservationHistory and table.getCurrentReservation() == reservation:
            reservation.updateStatus(ReservationStatus.CHECKED_IN)
            notification = Notification(f"Reservation {reservation.getReservationID()} is checked in. Table {table.getTableID()} is occupied.")
            notification.send()
            return True
        else:
            return False

    def freeTableForReservation(self, reservation, table):
        if reservation in self._reservationHistory and table.getCurrentReservation() == reservation:
            self.removeReservation(reservation)
            table.setCurrentReservation(None)
            table.setStatus(TableStatus.AVAILABLE)
            notification = Notification(f"Table {table.getTableID()} is now available.")
            notification.send()

    def takeTableOrder(self, table, meal):
        if table and table.getStatus() == TableStatus.RESERVED :
            table_order = TableOrder(table)
            table_order.addOrder(meal)
            table_order.updateStatus(OrderStatus.RECEIVED)
            return table_order
        else:
            return None

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) :
            return False
        branch = o
        if self._branchId != branch._branchId:
            return False
        if (self._name != branch._name) if self._name is not None else branch._name is not None:
            return False
        return self._location is branch._location if self._location is not None else branch._location is None

    def hashCode(self):
        result = hash(self._branchId)
        result = 31 * result + (hash(self._name) if self._name is not None else 0)
        result = 31 * result + (hash(self._location) if self._location is not None else 0)
        return result