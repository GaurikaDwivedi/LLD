import time
from .cash_deposit import CashDeposit
from .check_deposit import CheckDeposit
from .withdrawal import Withdrawal
class ATMPrinter:
    
    def __init__(self):
        pass

    def printReceipt(self, transaction):
        if transaction:
            print("Receipt Details:")
            print("Transaction ID:", transaction.transactionId)
            print("Transaction Status:", transaction.getStatus().name)
            print("Transaction Time:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(transaction.creationTime)))

            # Include additional details specific to the transaction type
            if isinstance(transaction, CashDeposit):
                print("Deposit Amount:", transaction.getAmount())
            elif isinstance(transaction, CheckDeposit):
                print(f"Check Details:\n ReceiverName: {transaction.getCheckDetails().getCustomer().getName()}, Bank: {transaction.getCheckDetails().getBankName()}, Amount: {transaction.getCheckDetails().getdepositAmount()}")
            elif isinstance(transaction, Withdrawal):
                print("Withdrawal Amount:", transaction.getfinalWithdrawnAmount())