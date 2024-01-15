class CreditCard:
    def __init__(self, cardHoldersName, cardNumber, expirationYear, expirationMonth, cvv, authority):
        self._cardHoldersName = cardHoldersName
        self._cardNumber = cardNumber
        self._expirationYear = expirationYear
        self._expirationMonth = expirationMonth
        self._cvv = cvv
        self._authority = authority

    def getCardHoldersName(self):
        return self._cardHoldersName

    def getCardNumber(self):
        return self._cardNumber

    def getExpirationYear(self):
        return self._expirationYear

    def getExpirationMonth(self):
        return self._expirationMonth

    def getCvv(self):
        return self._cvv

    def getAuthority(self):
        return self._authority