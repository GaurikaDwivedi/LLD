import time
from enum import Enum

class TransactionStatus(Enum):
    SUCCESS = 0
    FAILURE = 1
    PENDING = 2

class Transaction:

    def __init__(self, transactionId, accountThatInitiatedTransaction):
        self.status = 0
        self.transactionId = transactionId
        self.accountThatInitiatedTransaction = accountThatInitiatedTransaction
        self.creationTime = int(round(time.time() * 1000))

    def executeTransaction(self):
        pass

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    
    def getTransactionId(self):
        return self.transactionId
    
    def getAccount(self):
        return self.accountThatInitiatedTransaction