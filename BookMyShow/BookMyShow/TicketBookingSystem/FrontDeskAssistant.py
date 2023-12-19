from TicketBookingSystem.Member import Member

class FrontDeskAssistant(Member):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone)

    def createBookingAndIssueTicket(self, booking):
        pass

    def checkIn(self, booking):
        return booking.checkIn()
