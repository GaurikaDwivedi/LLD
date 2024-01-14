class Address:
    def __init__(self, streetAddress, city, state, zipcode, country):
        self._streetAddress = streetAddress
        self._city = city
        self._state = state
        self._zipCode = zipcode
        self._country = country

    def getStreetAddress(self):
        return self._streetAddress

    def getCity(self):
        return self._city

    def getState(self):
        return self._state

    def getZipCode(self):
        return self._zipCode

    def getCountry(self):
        return self._country
