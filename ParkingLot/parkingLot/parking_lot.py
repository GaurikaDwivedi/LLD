from parkingLot.vehicle import Vehicle, VehicleType
class ParkingLot:
    _parkingLot = None

    def __init__(self):
        self._id = None
        self._name = None
        self._location = None
        self._parkingFloors = []
        self._activeTickets = []
        self._unusedTicketPool = []
        self._entrances = []
        self._exits = []

    def addTicketToTicketPool(self, newTicket):
        self._unusedTicketPool.append(newTicket)

    @staticmethod
    def getInstance():
        if ParkingLot._parkingLot is None:
            ParkingLot._parkingLot = ParkingLot()
        return ParkingLot._parkingLot

    def issueNewParkingTicket(self, vehicle, entrance, ticket=None):
        if self.isFull(vehicle):
            entrance.displayMessage("Parking lot is full")
            return None
        if not self._unusedTicketPool:
            entrance.displayMessage("Sorry, we are out of tickets. Please come back later.")
            return None
        ticket.assignTicketTo(vehicle)
        vehicle.assignTicket(ticket)
        self.insertorUpdateToDB(vehicle, ticket, entrance)
        self._activeTickets.append(ticket)
        return ticket

    def isFull(self):
        for floor in self.getParkingFloors():
            if not floor.isFull1():
                return False
        return True

    def addParkingFloor(self, floor):
        self._parkingFloors.append(floor)

    def getParkingFloors(self):
        return self._parkingFloors

    def getEntrances(self):
        return self._entrances

    def setEntrances(self, entrances):
        self._entrances = entrances

    def addNewEntrance(self, entranceKiosk):
        self._entrances.append(entranceKiosk)

    def getExits(self):
        return self._exits

    def setExits(self, exits):
        self._exits = exits

    def addNewExit(self, exitKiosk):
        self._entrances.append(exitKiosk)