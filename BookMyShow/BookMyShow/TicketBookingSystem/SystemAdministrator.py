from TicketBookingSystem.Member import Member
from TicketBookingSystem.System import System

class SystemAdministrator(Member):
    def __init__(self, system, id, name, email, phone):
        super().__init__(id, name, email, phone)
        self._system = system or System()

    def addNewTheaterCompany(self, theaterCompany):
        self._system.addTheaterCompany(theaterCompany)

    def removeTheaterCompany(self, theaterCompany):
        self._system.removeTheaterCompany(theaterCompany)

    def getSystem(self):
        return self._system

    def setSystem(self, system):
        self._system = system
