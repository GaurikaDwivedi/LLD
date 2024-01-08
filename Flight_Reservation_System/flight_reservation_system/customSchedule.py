class CustomSchedule:
    def __init__(self, customDateTime):
        self._customDateTime = customDateTime
        self._day = []

    def getCustomDateTime(self):
        return self._customDateTime
    
    def setDay(self,day):
        self._day.append(day)

    def getDay(self):
        return self._day

    def setCustomDateTime(self, customDateTime):
        self._customDateTime = customDateTime

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != CustomSchedule:
            return False
        that = o
        return self._customDateTime == that._customDateTime

    def hashCode(self):
        return int((self._customDateTime ^ (self._customDateTime >> 32)))