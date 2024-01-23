class TableSeat:
    def __init__(self, id):
        self._identifier = id

    def getIdentifier(self):
        return self._identifier

    def setIdentifier(self, identifier):
        self._identifier = identifier

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != TableSeat:
            return False
        tableSeat = o
        return self._identifier == tableSeat._identifier

    def hashCode(self):
        return self._identifier