from .transaction import Transaction, TransactionStatus
class Withdrawal(Transaction):
    
    def __init__(self, transactionId, account, amount, cashDispenser, atm_instance):
        super().__init__(transactionId, account)
        self._amount = amount
        self._cashDispenser = cashDispenser
        self._atm_instance = atm_instance
        self._finalWithdrawnAmount = 0

    def getAmount(self):
        return self._amount
    
    def setfinalWithdrawnAmount(self, amount):
        self._finalWithdrawnAmount = amount
    
    def getfinalWithdrawnAmount(self):
        return self._finalWithdrawnAmount

    def executeTransaction(self):
        if self.accountThatInitiatedTransaction.withdrawFund(self._amount):
            if self._cashDispenser.dispenseCash(self._amount):
                self.setStatus(TransactionStatus.SUCCESS)
                self.setfinalWithdrawnAmount(self.getAmount())
            else:
                self.setStatus(TransactionStatus.FAILURE)
                self.accountThatInitiatedTransaction.addFund(self._amount)
        else:
            self.setStatus(TransactionStatus.FAILURE)
            self._atm_instance.displayMessage("Insufficient Balance!!")