class Passenger:
    def __init__(self, name, dateOfBirth, passportNumber):
        self.name = name
        self._dateOfBirth = dateOfBirth
        self.passportNumber = passportNumber

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPassportNumber(self):
        return self.passportNumber

    def setPassportNumber(self, passportNumber):
        self.passportNumber = passportNumber

    def getDateOfBirth(self):
        return self._dateOfBirth

    def setDateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth
