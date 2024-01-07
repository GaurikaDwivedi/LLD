class Education:

    def _initialize_instance_fields(self):
        self._schoolName = None
        self._degreeName = None
        self._startDate = 0
        self._enddate = 0

    def __init__(self, schoolName, degreeName, startDate, enddate):
        self._enddate = enddate
        self._initialize_instance_fields()

        self._schoolName = schoolName
        self._degreeName = degreeName
        self._startDate = startDate

    def getSchoolName(self):
        return self._schoolName

    def setSchoolName(self, schoolName):
        self._schoolName = schoolName

    def getDegreeName(self):
        return self._degreeName

    def setDegreeName(self, degreeName):
        self._degreeName = degreeName

    def getStartDate(self):
        return self._startDate

    def setStartDate(self, startDate):
        self._startDate = startDate

    def getEnddate(self):
        return self._enddate

    def setEnddate(self, enddate):
        self._enddate = enddate