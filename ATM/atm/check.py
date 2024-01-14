class Check:
    def __init__(self, customer, bankName, amount, accountNumber):
        self._customer = customer
        self._accountNumber = accountNumber
        self._bankName = bankName
        self._depositAmount= float(amount)

    def getBankName(self):
        return self._bankName

    def getCustomer(self):
        return self._customer

    def getdepositAmount(self):
        return self._depositAmount

    def getAccountNumber(self):
        return self._accountNumber