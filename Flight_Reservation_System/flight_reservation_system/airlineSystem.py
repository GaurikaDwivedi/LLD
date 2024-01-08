class AirlineSystem:
    def __init__(self):
        self._flights = []
        self._specificFlightInstances = []
        self._aircrafts = []

    def addFlight(self, flight):
        if not flight in self._flights:
            self._flights.append(flight)
            return True
        return False
    
    def getAvailableFlights(self):
        return self._flights

    def addSpecificFlightInstance(self, specificFlightInsatance):
        if not specificFlightInsatance in self._specificFlightInstances:
            self._specificFlightInstances.append(specificFlightInsatance)
            return True
        return False

    def addAircraft(self, aircraft):
        if not aircraft in self._aircrafts:
            self._aircrafts.append(aircraft)
            return True
        return False
    
    def getAircrafts(self):
        return self._aircrafts

    def removeFlight(self, flight):
        if flight in self._flights:
            self._flights.remove(flight)
            return True
        return False
    
    def removeSpecificFlightInstance(self, specificFlightInsatance):
        if specificFlightInsatance in self._specificFlightInstances:
            self._specificFlightInstances.remove(specificFlightInsatance)
            return True
        return False

    def removeAircraft(self, aircraft):
        if aircraft in self._aircrafts:
            self._aircrafts.remove(aircraft)
            return True
        return False

