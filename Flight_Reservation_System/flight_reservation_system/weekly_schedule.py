from enum import Enum


class Day(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class WeeklySchedule:
    def __init__(self, daysOfWeek, departureTime):
        self._daysOfWeek = daysOfWeek
        self._departureTime = departureTime

    def addNewDayOfWeek(self, day):
        if not day in self._daysOfWeek:
            self._daysOfWeek.append(day)
            return True
        return False

    def removeADayFromWeeklySchedule(self, day):
        if day in self._daysOfWeek:
            self._daysOfWeek.remove(day)
            return True
        return False
    
    def getDaysOfWeek(self):
        return self._daysOfWeek

    def setDaysOfWeek(self, daysOfWeek):
        self._daysOfWeek = daysOfWeek

    def getDepartureTime(self):
        return self._departureTime

    def setDepartureTime(self, departureTime):
        self._departureTime = departureTime

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != WeeklySchedule:
            return False
        that = o
        if not self._daysOfWeek is that._daysOfWeek:
            return False
        return self._departureTime == that._departureTime

    def hashCode(self):
        result = hash(self._daysOfWeek)
        result = 31 * result + hash(self._departureTime)
        return result