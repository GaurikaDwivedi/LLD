from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1
    COMPROMISED = 2

class RegisteredUser:
    def __init__(self, id, name, email, phone):
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone
        self._status = AccountStatus.ACTIVE

    def updateAccountStatus(self, accountStatus):
        self._status = accountStatus

    def updateEmail(self, email):
        self._email = email

    def updatePhone(self, phone):
        self._phone = phone

    def getId(self):
        return self._id
    
    def getStatus(self):
        return self._status

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getPhone(self):
        return self._phone
