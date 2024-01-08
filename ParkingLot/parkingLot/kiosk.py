class Kiosk:
    def __init__(self, kioskId):
        self._kioskId = kioskId

    def displayMessage(self, message):
        print(message)

class ExitKiosk(Kiosk):
    def __init__(self, kioskId):
        self._kioskId = None

        super().__init__(kioskId)

    def processPayment(self, ticket, customerCreditCard):
        ticket.markAsPaid()
        super().displayMessage("Payment processed successfully.")

class EntranceKiosk(Kiosk):
    def __init__(self, kioskId):
        self._kioskId = None

        super().__init__(kioskId)

    def issueTicket(self, vehicle, ticket=None):
        vehicle.assignTicket(ticket)
        super().displayMessage("Ticket issued successfully.")
