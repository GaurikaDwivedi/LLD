class ElectronicBankTransfer:

    def __init__(self, accountHoldersName, bankName, bankLocation, routingNumber, accountNumber):
        self._accountHoldersName = accountHoldersName
        self._bankName = bankName
        self._bankLocation = bankLocation
        self._routingNumber = routingNumber
        self._accountNumber = accountNumber

    def getAccountHoldersName(self):
        return self._accountHoldersName
    
    def getEncryptedBankName(self):
        return self._bankName
    
    def getEncryptedBankLocation(self):
        return self._bankLocation
    
    def getEncryptedRoutingNumber(self):
        return self._routingNumber
    
    def getEncryptedAccountNumber(self):
        return self._accountNumber