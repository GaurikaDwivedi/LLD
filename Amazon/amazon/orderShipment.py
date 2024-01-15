from amazon.shipmentStatus import ShipmentStatusUpdate

class OrderShipment:
    
    def __init__(self, shipmentNumber, shipmentDate, estimatedArrival, carrier):
        self._shipmentHistory = []
        self._shipmentNumber = shipmentNumber
        self._shipmentDate = shipmentDate
        self._estimatedArrival = estimatedArrival
        self._carrier = carrier

    def addShipmentHistory(self, shipmentStatusUpdate):
        self._shipmentHistory.append(shipmentStatusUpdate)

    def updateStatus(self, status):
        shipmentStatusUpdate = ShipmentStatusUpdate(self.getShipmentNumber(), status)
        self.addShipmentHistory(shipmentStatusUpdate)

    def getShipmentNumber(self):
        return self._shipmentNumber

    def getShipmentDate(self):
        return self._shipmentDate

    def getEstimatedArrival(self):
        return self._estimatedArrival

    def getCarrier(self):
        return self._carrier

    def getShipmentHistory(self):
        return self._shipmentHistory