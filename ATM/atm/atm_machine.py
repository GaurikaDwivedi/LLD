import uuid
from .atm_printer import ATMPrinter
from .balance_enquiry import BalanceInquiry
from .cash_deposit_slot import CashDepositSlot
from .cash_deposit import CashDeposit
from .check_deposit_slot import CheckDepositSlot
from .check_deposit import CheckDeposit
from .cash_dispense import CashDispense
from .keypad import Keypad
from .screen_display import ScreenDisplay
from .withdrawal import Withdrawal
from .constants import CardStatus

class ATM:
    _instance = None

    def __init__(self, atmID, location):
        self._currentCustomer = None
        self._mostRecentTransaction = None
        self._atmID = atmID
        self._location = location
        self._keypad = Keypad()
        self._screen = ScreenDisplay()
        self._printer = ATMPrinter()
        self._checkDepositSlot = CheckDepositSlot(atm_instance=self)
        self._cashDepositSlot = CashDepositSlot(atm_instance=self)
        self._cashDepenser = CashDispense(atm_instance=self)

    @staticmethod
    def getInstance(atmID, location):
        if ATM._instance is None:
            ATM._instance = ATM(atmID, location)
        return ATM._instance
    
    def authenticateUser(self, card):
        card_status = card.getStatus()
        if card_status == CardStatus.ACTIVE:
            self.loginCustomer(card.getCustomer())
            pin = input("Enter Pin: ")
            if pin == card.getPin():
                return True
            else:
                return False
        else:
            self.displayMessage(f"Card Status:{card.getStatus().name}")
            return False

    def logoutCustomer(self):
        self._currentCustomer = None

    def loginCustomer(self, customer):
        self._currentCustomer = customer

    def setRecentTransaction(self, transaction):
        self._mostRecentTransaction = transaction

    def depositCash(self, amount):
        uniqueTransactionId = str(uuid.uuid1())
        cash_deposit_transaction =  CashDeposit(uniqueTransactionId, self.getCustomerAccount(), amount, self.getCashDepositSlot(), atm_instance=self)
        cash_deposit_transaction.depositCash()
        self.setRecentTransaction(cash_deposit_transaction)
        self.printReceipt()

    def depositCheck(self, check):
        uniqueTransactionId = str(uuid.uuid1())
        check_deposit_transaction =   CheckDeposit(uniqueTransactionId, self.getCustomerAccount(), check, self.getCheckDepositSlot(), atm_instance=self)
        check_deposit_transaction.depositCheck(check)
        self.setRecentTransaction(check_deposit_transaction)
        self.printReceipt()

    def balanceInquiry(self):
        uniqueTransactionId = str(uuid.uuid1())
        balance_enquiry_transaction = BalanceInquiry(uniqueTransactionId, self.getCustomerAccount())
        message = balance_enquiry_transaction.getBalance()
        self.setRecentTransaction(balance_enquiry_transaction)
        self.printReceipt()
        return message

    def withdrawCash(self, amountToBeWithdrawn):
        uniqueTransactionId = str(uuid.uuid1())
        withdraw_transaction = Withdrawal(uniqueTransactionId, self.getCustomerAccount(), amountToBeWithdrawn,
                                           self.getCashDispenser(), atm_instance=self)
        withdraw_transaction.executeTransaction()
        self.setRecentTransaction(withdraw_transaction)
        self.printReceipt()

    def changePin(self, newPin):
        self._currentCustomer.getCardAssociatedWithThisAccount().changePin(newPin)

    def printReceipt(self):
        if self._mostRecentTransaction is not None:
            self._printer.printReceipt(self._mostRecentTransaction)

    def displayMessage(self, message):
        self._screen.showMessage(message)

    def getCashDispenser(self):
        return self._cashDepenser
    
    def getCashDepositSlot(self):
        return self._cashDepositSlot
    
    def getCheckDepositSlot(self):
        return self._checkDepositSlot
    
    def getCustomerAccount(self):
        if self._currentCustomer:
            return self._currentCustomer.getAccount()
        else:
            print("Error: No customer logged in.")
            return None