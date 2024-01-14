from .constants import CardStatus

class ATMCard:
    def __init__(self, cardNumber, expirationDate, cvv):
        self._customer = None
        self._pin = 0
        self._cardNumber = cardNumber
        self._expirationDate = expirationDate
        self._cvv = cvv
        self._status = CardStatus.NOT_YET_ACTIVATED

    def activateCard(self):
       self.setStatus(CardStatus.ACTIVE)

    def blockCard(self):
        self.setStatus(CardStatus.BLOCKED)

    def closeAccount(self):
        self.setStatus(CardStatus.ACCOUNT_CLOSED)

    def markAsCompromised(self):
        self.setStatus(CardStatus.COMPROMISED)

    def getCardNumber(self):
        return self._cardNumber
    
    def getCustomer(self):
        return self._customer

    def getExpirationDate(self):
        return self._expirationDate

    def getPin(self):
        return self._pin

    def getCvv(self):
        return self._cvv

    def getStatus(self):
        return self._status

    def setCustomer(self, customer):
        self._customer = customer

    def setPin(self, newPin):
        self._pin = newPin

    def setStatus(self, status):
        self._status = status