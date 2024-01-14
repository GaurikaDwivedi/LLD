from .deposit import Deposit
from .transaction import TransactionStatus

class CashDeposit(Deposit):
    
    def __init__(self, transactionId, customerAccount, amount, cashDepositSlot, atm_instance):
        super().__init__(transactionId, customerAccount)
        self.setdepositAmount(amount)
        self._cashDepositSlot = cashDepositSlot
        self._atm_instance = atm_instance
    
    def depositCash(self):
        amount = self.getAmount()
        if self._cashDepositSlot.processDeposit(amount):
            self.executeTransaction()
        if self.getStatus() == TransactionStatus.SUCCESS:
            self._atm_instance.displayMessage("Transaction Successful!!")
            return True
        else:
            self._atm_instance.displayMessage("Transaction Failed. Try Later.")
            return False