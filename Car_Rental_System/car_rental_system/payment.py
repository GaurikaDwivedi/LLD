from enum import Enum

class PaymentStatus(Enum):
    UNPAID = 0
    PENDING = 1
    COMPLETED = 2
    DECLINED = 3
    REFUNDED = 4

class Payment:
    def __init__(self, transactionId):
        self._paymentStatus = 0
        self._transactionId = transactionId

    def getTransactionId(self):
        return self._transactionId

    def getPaymentStatus(self):
        return self._paymentStatus

    def setPaymentStatus(self, paymentStatus):
        self._paymentStatus = paymentStatus