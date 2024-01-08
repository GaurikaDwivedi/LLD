class Flight:

    def _initialize_instance_fields(self):
        self._flightNumber = None
        self._departure = None
        self._arrival = None
        self._durationInMinutes = 0
        self._aircraft = None
        self._weeklySchedules = []
        self._customSchedules = []
        self._gateAssignment = {}
        self.flightStatus = {}
        self._flight = None

    def __init__(self, flightNumber, departure, arrival, durationInMinutes, aircraft):
        self._initialize_instance_fields()  
        self._flightNumber = flightNumber
        self._departure = departure
        self._arrival = arrival
        self._durationInMinutes = durationInMinutes
        self._aircraft = aircraft

    @staticmethod
    def updateStatus(self, flightDateTime, status):
        self.flightStatus[flightDateTime] = status

    def assignOrReassignGate(self, flightDateTime, gateNumber):
        self._gateAssignment[flightDateTime] = gateNumber

    def getAssignedGateNumber(self, flightDateTime):
        return self._gateAssignment[flightDateTime]
    
    def getFlightNumber(self):
        return self._flightNumber
    
    def getDeparture(self):
        return self._departure

    def getFlightStatus(self, flightDateTime):
        return self.flightStatus[flightDateTime]
    
    def addNewWeeklySchedule(self, weeklySchedule):
        if (weeklySchedule) not in self._weeklySchedules:
            self._weeklySchedules.append(weeklySchedule)
            return True
        return False

    def removeWeeklySchedule(self, weeklySchedule):
        if (weeklySchedule) in self._weeklySchedules:
            self._weeklySchedules.remove(weeklySchedule)
            return True
        return False

    def addNewCustomSchedule(self, customSchedule):
        if not (customSchedule) in self._customSchedules:
            self._customSchedules.append(customSchedule)
            return True
        return False

    def removeCustomSchedule(self, customSchedule):
        if (customSchedule) in self._customSchedules:
            self._customSchedules.remove(customSchedule)
            return True
        return False

    def getWeeklySchedules(self):
        return self._weeklySchedules

    def setWeeklySchedules(self, weeklySchedules):
        self._weeklySchedules = weeklySchedules

    def getCustomSchedules(self):
        return self._customSchedules
    
    def setCustomSchedules(self, customSchedules):
        self._customSchedules = customSchedules

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Flight:
            return False
        flight = o
        if self._durationInMinutes != flight._durationInMinutes:
            return False
        if self._flightNumber != flight._flightNumber:
            return False
        if (not self._departure is flight._departure) if self._departure is not None else flight._departure is not None:
            return False
        if (not self._arrival is flight._arrival) if self._arrival is not None else flight._arrival is not None:
            return False
        return self._aircraft is flight._aircraft if self._aircraft is not None else flight._aircraft is None

    def hashCode(self):
        result = hash(self._flightNumber)
        result = 31 * result + (hash(self._departure) if self._departure is not None else 0)
        result = 31 * result + (hash(self._arrival) if self._arrival is not None else 0)
        result = 31 * result + self._durationInMinutes
        result = 31 * result + (hash(self._aircraft) if self._aircraft is not None else 0)
        return result
