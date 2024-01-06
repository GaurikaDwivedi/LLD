class DriverLicense:
    def __init__(self, licenceNumber, stateWhichIssuedLicense, driverName, dateIssued, validTill):
        self._licenceNumber = licenceNumber
        self._stateWhichIssuedLicense = stateWhichIssuedLicense
        self._DriverName = driverName
        self._dateIssued = dateIssued
        self._validTill = validTill

    def getLicenceNumber(self):
        return self._licenceNumber

    def setLicenceNumber(self, licenceNumber):
        self._licenceNumber = licenceNumber

    def getStateWhichIssuedLicense(self):
        return self._stateWhichIssuedLicense

    def setStateWhichIssuedLicense(self, stateWhichIssuedLicense):
        self._stateWhichIssuedLicense = stateWhichIssuedLicense

    def getDriverName(self):
        return self._DriverName

    def setDriverName(self, driverName):
        self._DriverName = driverName

    def getDateIssued(self):
        return self._dateIssued
    
    def setDateIssued(self, dateIssued):
        self._dateIssued = dateIssued

    def getValidTill(self):
        return self._validTill

    def setValidTill(self, validTill):
        self._validTill = validTill
