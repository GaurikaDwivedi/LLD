class User:
    def __init__(self, name, address, email, phone):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone