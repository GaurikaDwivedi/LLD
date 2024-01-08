class CreditCard:
    def __init__(self, cardHoldersName, cardNumber, expirationYear, expirationMonth, cvv, authority):
        self._cardHoldersName = cardHoldersName
        self._cardNumber = cardNumber
        self._expirationYear = expirationYear
        self._expirationMonth = expirationMonth
        self.cvv = cvv
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
        return self.cvv

    def getAuthority(self):
        return self._authority
    
    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != CreditCard:
            return False
        that = o
        if self._cardNumber != that._cardNumber:
            return False
        if self._expirationYear != that._expirationYear:
            return False
        if self._expirationMonth != that._expirationMonth:
            return False
        return self.cvv is that.cvv

    def hashCode(self):
        result = hash(self._cardNumber)
        result = 31 * result + hash(self._expirationYear)
        result = 31 * result + hash(self._expirationMonth)
        result = 31 * result + hash(self.cvv)
        return result
