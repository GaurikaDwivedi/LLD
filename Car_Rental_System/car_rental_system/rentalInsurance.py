from enum import Enum
class InsuranceCoverageType(Enum):
        REGULAR = 0
        ADVANCED = 1

class RentalInsurance:

    def __init__(self, insuranceId, issuingInsuranceCompany, startDate, endDate, coverageType, ratePerDay):
        self._insuranceId = insuranceId
        self._issuingInsuranceCompany = issuingInsuranceCompany
        self._startDate = startDate
        self._endDate = endDate
        self._coverageType = coverageType
        self.ratePerDay = ratePerDay

    def getInsuranceId(self):
        return self._insuranceId

    def setInsuranceId(self, insuranceId):
        self._insuranceId = insuranceId

    def getIssuingInsuranceCompany(self):
        return self._issuingInsuranceCompany

    def setIssuingInsuranceCompany(self, issuingInsuranceCompany):
        self._issuingInsuranceCompany = issuingInsuranceCompany

    def getStartDate(self):
        return self._startDate

    def setStartDate(self, startDate):
        self._startDate = startDate

    def getEndDate(self):
        return self._endDate

    def setEndDate(self, endDate):
        self._endDate = endDate

    def getCoverageType(self):
        return self._coverageType

    def setCoverageType(self, coverageType):
        self._coverageType = coverageType

    def getRatePerDay(self):
        return self.ratePerDay

    def setRatePerDay(self, ratePerDay):
        self.ratePerDay = ratePerDay