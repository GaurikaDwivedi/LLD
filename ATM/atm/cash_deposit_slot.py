from .deposit_slot import DepositSlot
from .cash_deposit import CashDeposit

class CashDepositSlot(DepositSlot):

    def __init__(self, atm_instance):
        self._atm_instance = atm_instance

    def processDeposit(self, amount):
        self._scanCashDeposited()
        if self._validateDeposit(amount):
            self._atm_instance.displayMessage(f"Processing....\nPlease wait..")
            return True
        else:
            self._atm_instance.displayMessage("Invalid deposit. Please try again.")
            return False

    def _validateDeposit(self, amount):
        return amount > 0

    def _scanCashDeposited(self):
        self._atm_instance.displayMessage("scanning!!")