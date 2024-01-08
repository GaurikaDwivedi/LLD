from enum import Enum

class PaymentStatus(Enum):
    PENDING = 0
    PAID = 1
    DECLINED = 2
    REFUNDED = 3

class Payment:
    def __init__(self, transactionId, reservationPaymentMadeFor):
        self._paymentStatus = 0
        self._transactionId = transactionId
        self._reservationPaymentMadeFor = reservationPaymentMadeFor

    def getTransactionId(self):
        return self._transactionId

    def setTransactionId(self, transactionId):
        self._transactionId = transactionId

    def getPaymentStatus(self):
        return self._paymentStatus

    def setPaymentStatus(self, paymentStatus):
        self._paymentStatus = paymentStatus

    def getReservationPaymentMadeFor(self):
        return self._reservationPaymentMadeFor
    
    def setReservationPaymentMadeFor(self, reservationPaymentMadeFor):
        self._reservationPaymentMadeFor = reservationPaymentMadeFor