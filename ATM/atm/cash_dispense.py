class CashDispense:

    def __init__(self, atm_instance):
        self._atm_instance = atm_instance
        self._available_cash = 1000  # Assuming an initial amount of cash available in the ATM

    def addAvailableCash(self, amount): # By Bank we add money to machine
        self._available_cash += amount

    def deductAvailableCash(self, amount):
         self._available_cash -= amount

    def dispenseCash(self, amount):
        if self._validateDispense(amount):
            self._atm_instance.displayMessage(f"Dispensing Rs. {amount}")
            self.deductAvailableCash(amount)
            return True
        else:
            self._atm_instance.displayMessage("Insufficient funds in the ATM. Unable to dispense cash.")
            self._atm_instance.displayMessage("If amount is deducted from your account, it'll be processed back in 48hours.")
            return False

    def _validateDispense(self, amount):
        return amount <= self._available_cash