from .transaction import Transaction, TransactionStatus
class Deposit(Transaction):
    def __init__(self, transactionId, Account):
        self.amount = 0
        self.depositSlot = None
        super().__init__(transactionId, Account)

    def getAmount(self):
        return self.amount
    
    def setdepositAmount(self, amount):
        self.amount = amount
    
    def executeTransaction(self):
        if self.accountThatInitiatedTransaction.addFund(self.amount):
            self.setStatus(TransactionStatus.SUCCESS)
        else:
            self.setStatus(TransactionStatus.FAILURE)