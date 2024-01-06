class CarRentalLocation:
    def __init__(self, locationId, locationName, streetAddress, city, state, zipCode, country):
        self._locationId = locationId
        self._locationName = locationName
        self._streetAddress = streetAddress
        self._city = city
        self._state = state
        self._zipCode = zipCode
        self._country = country

    def getLocationId(self):
        return self._locationId

    def setLocationId(self, locationId):
        self._locationId = locationId

    def getLocationName(self):
        return self._locationName

    def setLocationName(self, locationName):
        self._locationName = locationName

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
        if o is None or type(o) != CarRentalLocation:
            return False
        that = o
        if self._locationId != that._locationId:
            return False
        if (
                self._locationName != that._locationName) if self._locationName is not None else that._locationName is not None:
            return False
        if (
                self._streetAddress != that._streetAddress) if self._streetAddress is not None else that._streetAddress is not None:
            return False
        if (self._city != that._city) if self._city is not None else that._city is not None:
            return False
        if (self._state != that._state) if self._state is not None else that._state is not None:
            return False
        if (self._zipCode != that._zipCode) if self._zipCode is not None else that._zipCode is not None:
            return False
        return self._country == that._country if self._country is not None else that._country is None

    def hashCode(self):
        result = hash(self._locationId)
        result = 31 * result + (hash(self._locationName) if self._locationName is not None else 0)
        result = 31 * result + (hash(self._streetAddress) if self._streetAddress is not None else 0)
        result = 31 * result + (hash(self._city) if self._city is not None else 0)
        result = 31 * result + (hash(self._state) if self._state is not None else 0)
        result = 31 * result + (hash(self._zipCode) if self._zipCode is not None else 0)
        result = 31 * result + (hash(self._country) if self._country is not None else 0)
        return result
