import time
from enum import Enum

class ShipmentStatus(Enum):
    PENDING = 0
    PLACED = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4
    RETURN_REQUESTED = 5

class ShipmentStatusUpdate:

    def __init__(self, shipmentNumber, status):
        self._shipmentNumber = shipmentNumber
        self._status = status
        self._creationDate = round(time.time() * 1000)

    def getStatus(self):
        return self._status

    def getCreationDate(self):
        return self._creationDate

    def getShipmentNumber(self):
        return self._shipmentNumber
    