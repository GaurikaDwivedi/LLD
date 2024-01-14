from .deposit import Deposit
from .transaction import TransactionStatus

class CheckDeposit(Deposit):

    def __init__(self, transactionId, customerAccountNumber, check, checkDepositSlot, atm_instance):
        super().__init__(transactionId, customerAccountNumber)
        self._checkDepositSlot = checkDepositSlot
        self._atm_instance = atm_instance
        self._check = check
        self.setdepositAmount(self.getCheckDetails().getdepositAmount())

    def getCheckDetails(self):
        return self._check

    def depositCheck(self, check):
        if self._checkDepositSlot.processDeposit(check):
            self.executeTransaction()
        if self.getStatus() == TransactionStatus.SUCCESS:
            self._atm_instance.displayMessage("Transaction Successful!!")
            return True
        else:
            self._atm_instance.displayMessage("Transaction Failed. Try Later.")
            return False