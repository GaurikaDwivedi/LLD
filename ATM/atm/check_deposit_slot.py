from .deposit_slot import DepositSlot
class CheckDepositSlot(DepositSlot):
    def __init__(self, atm_instance):
        self._atm_instance = atm_instance
        self._init()

    def processDeposit(self, check):
        amount = check.getdepositAmount()
        if self._validateDeposit(amount):
            self._atm_instance.displayMessage(f"Processing....\nPlease wait..")
            return True
        else:
            self._atm_instance.displayMessage("Invalid deposit. Please try again.")
            return False

    def _validateDeposit(self, amount):
        return amount > 0

    def _scanCheck(self):
        pass

    def _init(self):
        pass