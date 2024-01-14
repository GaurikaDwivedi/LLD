from atm.atm_machine import ATM
from atm.atm_card import ATMCard
from atm.customer import Customer
from atm.account import Account
from atm.bank import Bank
from atm.address import Address
from atm.check import Check

# Create a bank
bank = Bank(name="Example Bank", bankCode="123", branchLocation="Main Branch")

# Create an ATM instance
atm_address = Address(streetAddress="123 Main St", city="City1", state="State", zipcode="12945", country="Country1")
atm = ATM.getInstance(atmID="ATM001", location=atm_address)

# Create a customer
customer_address = Address(streetAddress="123 Main St", city="City", state="State", zipcode="12345", country="Country")
customer_account = Account(accountNumber="ACC001", bank=bank)
customer = Customer(name="John Doe", email="john.doe@example.com", account=customer_account, address=customer_address, phone="1234567890")

# Create an ATM card for the customer
atm_card = ATMCard(cardNumber="1234-5678-9012-3456", expirationDate="12/25", cvv="123")
atm_card.setCustomer(customer)
customer.assignCard(atm_card)
customer.activateCard()
customer.setPin(pin="1234")
#bank.blockCard(atm_card)   #un-comment this to try-out blocked card 
# Authenticate the user (card) with the ATM
authenticated = atm.authenticateUser(atm_card)

# Perform operations
while authenticated:
    print("User authenticated. Select a transaction option:")
    print("1. Deposit Cash")
    print("2. Deposit Check")
    print("3. Withdraw Cash")
    print("4. Balance Inquiry")
    print("5. Change PIN")
    print("6. Logout")
    user_option = input("Enter the option number: ")

    # Perform the selected transaction based on user input
    if user_option == "1":
        amount = float(input("Enter the deposit amount: "))
        atm.depositCash(amount)
    elif user_option == "2":
        check =  Check(customer =customer, accountNumber=customer_account.getAccountNumber(), bankName=customer_account.getBank().getName(), amount=100)
        atm.depositCheck(check)
    elif user_option == "3":
        # Assuming user input for the withdrawal amount
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        atm.withdrawCash(withdrawal_amount)
    elif user_option == "4":
        message = atm.balanceInquiry()
        atm.displayMessage(message)
    elif user_option == "5":
        new_pin = input("Enter the new PIN: ")
        if len(new_pin)!=4:
            atm.displayMessage("PIN should of 4 digits.")
        else:
            atm_card.setPin(new_pin)
            atm.displayMessage("PIN changed Successfully.")
            atm.logoutCustomer()
            authenticated = False
            atm.displayMessage("Enter new PIN to authenticate.")
            authenticated = atm.authenticateUser(atm_card)
    elif user_option == "6":
        atm.logoutCustomer()
        atm.displayMessage("Logged out.")
        authenticated = False
    else:
        print("Invalid option. Please choose a valid option.")
else:
    print("Authentication failed. Please check your card and PIN.")