class Employee:
    def __init__(self, name, email, phone, employeeID, dateJoined):
        self._name = name
        self._email = email
        self._phone = phone
        self._employeeID = employeeID
        self._dateJoined = dateJoined

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def getEmployeeID(self):
        return self._employeeID

    def setEmployeeID(self, employeeID):
        self._employeeID = employeeID

    def getDateJoined(self):
        return self._dateJoined

    def setDateJoined(self, dateJoined):
        self._dateJoined = dateJoined
