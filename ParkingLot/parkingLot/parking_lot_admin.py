from .user import User
from .parking_lot import ParkingLot
class ParkingLotAdministrator(User):
    def Administrator(self, employeeId, name, email, phone):
        super().__init__(employeeId, name, email, phone)

    def addParkingFloorToSystem(self, floor):
        ParkingLot.getInstance().addParkingFloor(floor)

    def addParkingSpot(self, floor, spot):
        try:
            floor.addParkingSpot(spot)
        except Exception as ex:
            print(ex.getMessage())

    def generateNewTicket(self, ticket):
        ParkingLot.getInstance().addTicketToTicketPool(ticket)

    def addNewEntrance(self, entranceKiosk):
        ParkingLot.getInstance().addNewEntrance(entranceKiosk)

    def addNewExit(self, exitKiosk):
        ParkingLot.getInstance().addNewExit(exitKiosk)