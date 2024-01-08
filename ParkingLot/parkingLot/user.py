class User:
    def __init__(self, employeeId, name, email, phone):
        self.employeeId = employeeId
        self.name = name
        self.email = email
        self.phone = phone

    def getEmployeeId(self):
        return self.employeeId

    def updateEmployeeId(self, employeeId):
        self.employeeId = employeeId

    def getName(self):
        return self.name

    def updateName(self, name):
        self.name = name

    def getEmail(self):
        return self.email

    def updateEmail(self, email):
        self.email = email

    def getPhone(self):
        return self.phone

    def updatePhone(self, phone):
        self.phone = phone
