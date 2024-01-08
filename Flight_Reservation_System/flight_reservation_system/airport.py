class Airport:
    def __init__(self, name, address, code):
        self._name = name
        self._address = address
        self._code = code
        self._flights = []

    def addNewFlight(self, flight):
        if not flight in self._flights:
            self._flights.append(flight)
        return False

    def removeFlight(self, flight):
        if flight in self._flights:
            self._flights.remove(flight)
        return False

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def getCode(self):
        return self._code

    def setCode(self, code):
        self._code = code

    def getFlights(self):
        return self._flights

    def setFlights(self, flights):
        self._flights = flights

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Airport:
            return False
        airport = o
        if (self._name != airport._name) if self._name is not None else airport._name is not None:
            return False
        return self._code == airport._code

    def hashCode(self):
        result = hash(self._name) if self._name is not None else 0
        result = 31 * result + hash(self._code)
        return result

    