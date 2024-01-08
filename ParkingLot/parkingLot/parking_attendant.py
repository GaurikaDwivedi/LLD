from .user import User
class ParkingAttendant(User):
    def __init__(self, employeeId, name, email, phone):
        self._paymentProcessor = None

        super().__init__(employeeId, name, email, phone)

    def issueTicket(self, vehicle):
        pass

    def processTicketAndCollectPayment(self, TicketNumber):
        pass

    def setPaymentProcessor(self, kiosk):
        self._paymentProcessor = kiosk