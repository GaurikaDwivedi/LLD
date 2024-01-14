from .transaction import Transaction, TransactionStatus

class BalanceInquiry(Transaction):

    def __init__(self, transactionId, customerAccountNumber):
        super().__init__(transactionId, customerAccountNumber)

    def getBalance(self):
        self.setStatus(TransactionStatus.SUCCESS)
        return "Available Balance: " + str(self.accountThatInitiatedTransaction.getAvailableBalance())