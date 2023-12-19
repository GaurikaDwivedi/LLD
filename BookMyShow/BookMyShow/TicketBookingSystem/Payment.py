import time
from enum import Enum


class PaymentStatus(Enum):
    UNPAID = 0
    PENDING = 1
    COMPLETED = 2
    DECLINED = 3
    CANCELLED = 4
    REFUNDED = 5

class PaymentMethod(Enum):
        CASH = 0
        CREDIT_CARD = 1


class Payment:
    def __init__(self, amount, transactionId, status, paymentMethod):
        self._status = status
        self._amount = amount
        self._createdOn = round(time.time() * 1000)
        self._transactionId = transactionId
        self._paymentMethod = paymentMethod

    def updatePauymentStatus(self, status):
        self._status = status

    def getAmount(self):
        return self._amount

    def getCreatedOn(self):
        return self._createdOn

    def getTransactionId(self):
        return self._transactionId

    def getStatus(self):
        return self._status

    def getPaymentMethod(self):
        return self._paymentMethod

    def setPaymentMethod(self, paymentMethod):
        self._paymentMethod = paymentMethod
