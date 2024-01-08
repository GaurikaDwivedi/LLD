class Address:
    def __init__(self, streetAddress, city, state, zipCode, country):
        self._streetAddress = streetAddress
        self._city = city
        self._state = state
        self._zipCode = zipCode
        self._country = country

    def getStreetAddress(self):
        return self._streetAddress

    def setStreetAddress(self, streetAddress):
        self._streetAddress = streetAddress

    def getCity(self):
        return self._city

    def setCity(self, city):
        self._city = city

    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state

    def getZipCode(self):
        return self._zipCode

    def setZipCode(self, zipCode):
        self._zipCode = zipCode

    def getCountry(self):
        return self._country

    def setCountry(self, country):
        self._country = country

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Address:
            return False
        address = o
        if self._streetAddress != address._streetAddress:
            return False
        if self._city != address._city:
            return False
        if self._state != address._state:
            return False
        if self._zipCode != address._zipCode:
            return False
        return self._country == address._country

    def hashCode(self):
        result = hash(self._streetAddress)
        result = 31 * result + hash(self._city)
        result = 31 * result + hash(self._state)
        result = 31 * result + hash(self._zipCode)
        result = 31 * result + hash(self._country)
        return result