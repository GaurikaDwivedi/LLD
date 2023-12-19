class System:
    def __init__(self):
        self._theater_companies = []

    def addTheaterCompany(self, theater_company):
        self._theater_companies.append(theater_company)

    def removeTheaterCompany(self, theater_company):
        if theater_company in self._theater_companies:
            self._theater_companies.remove(theater_company)

    def getTheaterCompanies(self):
        return self._theater_companies
