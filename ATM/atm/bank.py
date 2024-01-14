from .constants import CardStatus

class Bank:
    def __init__(self, name, bankCode, branchLocation):
        self._name = name
        self._bankCode = bankCode
        self._branchLocation = branchLocation

    def getName(self):
        return self._name

    def getBranchLocation(self):
        return self._branchLocation
    
    def getBankCode(self):
        return self._bankCode
    
    def blockCard(self, card):
        card.setStatus(CardStatus.BLOCKED)