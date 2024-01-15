from amazon.notification import Notification
class Payment:

    def _initialize_instance_fields(self):
        self._customer = None
        self._amount = 0
        self._creditCard = None
        self._electronicBankTransfer = None

    def __init__(self, customer, amount, electronicBankTransfer, creditCard=None):
        self._initialize_instance_fields()
        self._creditCard = creditCard
        self._customer = customer
        self._amount = amount
        self._electronicBankTransfer = electronicBankTransfer

    def refund(self, refund_amount):
        if self._creditCard is not None:
            notification = Notification(f"Refund of {refund_amount} is processed to credit card with details:\n"
                                        f"Card No.: {self.getCreditCard().getCardNumber()}.\n"
                                        f"Card Holder Name.: {self.getCreditCard().getCardHoldersName()}.\n")
        elif self._electronicBankTransfer is not None:
            notification = Notification(f"Refund of {refund_amount} is processed to bank account.\n"
                                        f"Account No.: {self.getElectronicBankTransfer().getEncryptedAccountNumber()}.\n"
                                        f"Account Holder Name.: {self.getElectronicBankTransfer().getAccountHoldersName()}.\n")
        else:
            notification = Notification("Refund failed. No payment method specified.")
        notification.send()

    def getCustomer(self):
        return self._customer

    def getAmount(self):
        return self._amount

    def getCreditCard(self):
        return self._creditCard
    
    def getElectronicBankTransfer(self):
        return self._electronicBankTransfer
