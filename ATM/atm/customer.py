
class Customer:
    def __init__(self, name, email, account, address, phone):
        self._cardAssociatedWithThisAccount = None
        self._name = name
        self._email = email
        self._account = account
        self._phone = phone
        self._billingAdddress = address

    def assignCard(self, card):
        self._cardAssociatedWithThisAccount = card

    def activateCard(self):
        self.getCardAssociatedWithThisAccount().activateCard()
    
    def setPin(self,pin):
        self.getCardAssociatedWithThisAccount().setPin(pin)

    def makeTransaction(self, transaction):
        return transaction.executeTransaction()

    def getBillingAddress(self):
        return self._billingAdddress

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getPhone(self):
        return self._phone

    def getBillingAdddress(self):
        return self._billingAdddress

    def getCardAssociatedWithThisAccount(self):
        return self._cardAssociatedWithThisAccount

    def getAccount(self):
        return self._account
    