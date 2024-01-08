class Aircraft:
    def __init__(self, name, model, manufacturingYear, seats):
        self._aircraftId = None
        self._name = name
        self._model = model
        self._manufacturingYear = manufacturingYear
        self._seats = seats

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    def getManufacturingYear(self):
        return self._manufacturingYear

    def setManufacturingYear(self, manufacturingYear):
        self._manufacturingYear = manufacturingYear

    def getSeats(self):
        return self._seats

    def setSeats(self, seats):
        self._seats = seats

    def getAircraftId(self):
        return self._aircraftId

    def setAircraftId(self, aircraftId):
        self._aircraftId = aircraftId

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Aircraft:
            return False
        aircraft = o
        if self._manufacturingYear != aircraft._manufacturingYear:
            return False
        if self._aircraftId != aircraft._aircraftId:
            return False
        if (self._name != aircraft._name) if self._name is not None else aircraft._name is not None:
            return False
        return self._model == aircraft._model if self._model is not None else aircraft._model is None

    def hashCode(self):
        result = hash(self._aircraftId)
        result = 31 * result + (hash(self._name) if self._name is not None else 0)
        result = 31 * result + (hash(self._model) if self._model is not None else 0)
        result = 31 * result + self._manufacturingYear
        return result