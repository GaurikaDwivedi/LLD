class Bounty:
    def __init__(self, reputation, expirationDate):
        self._reputation = reputation
        self._expirationdate = expirationDate

    def modifyReputation(self, reputation):
        self._reputation = reputation