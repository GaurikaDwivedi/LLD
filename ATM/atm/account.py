class Account:
    def __init__(self, accountNumber, bank):
        self._availableBalance = 0
        self._accountNumber = accountNumber
        self._bank = bank

    def addFund(self, amount):
        self._availableBalance += amount
        return True

    def withdrawFund(self, amount):
        if amount<=self._availableBalance:
            self._availableBalance -= amount
            return True
        else:
            return False

    def getAccountNumber(self):
        return self._accountNumber

    def getAvailableBalance(self):
        return self._availableBalance
    
    def getBank(self):
        return self._bank
