from .registeredUser import RegisteredUser, AccountStatus
from .cart import Cart

class Customer(RegisteredUser):
    def __init__(self, id, name, email, phone):
        self._isPrimeMember = False
        self._creditCards = []
        self._bankAccounts = []
        self._cart = Cart()
        self._orders = []
        self._shippingAddresses = []

        super().__init__(id, name, email, phone)

    def isRegistered(self):
        # Check if the customer is a registered user based on your criteria
        return isinstance(self, RegisteredUser)

    def isAccountActive(self):
        return self.getStatus() == AccountStatus.ACTIVE

    def getShoppingCart(self):
        return self._cart

    def addItemToCart(self, item, quantity):
        self._cart.addItem(item, quantity)

    def removeItemFromCart(self, item):
        if self._cart.getItems().containsKey(item):
            self._cart.removeItem(item)
            return True
        return False

    def addProductReview(self, review):
        review.getProduct().addReview(review)

    def placeOrder(self, order, order_shipment, payment):
        if self.isRegistered() and self.isAccountActive():
            order.makePayment(payment)
            order.ship(order_shipment)  # Mark the order as shipped
            self._orders.append(order)  # Add the order to the customer's list of orders
            self.getShoppingCart().clear()  # Clear the shopping cart after placing the order
            return True
        return False

    def CheckisPrimeMember(self):
        return self._isPrimeMember

    def subscribeToPrimeMembership(self):
        self._isPrimeMember = True

    def expirePrimeMembership(self):
        self._isPrimeMember = False

    def getCreditCards(self):
        return self._creditCards

    def addCreditCard(self, creditCard):
        if not creditCard in self._creditCards:
            self._creditCards.append(creditCard)
            return True
        return False

    def getBankAccounts(self):
        return self._bankAccounts
    
    def setBankAccount(self, bankAccount):
        if not bankAccount in self._bankAccounts:
            self._bankAccounts.append(bankAccount)
            return True
        return False

    def getCart(self):
        return self._cart

    def addToCart(self, item, quantity):
        self._cart.addItem(item, quantity)

    def getOrders(self):
        return self._orders

    def setOrders(self, orders):
        self._orders = orders

    def getShippingAddresses(self):
        return self._shippingAddresses 

    def addShippingAddress(self, shippingAddress):
        if not shippingAddress in self._shippingAddresses:
            self._shippingAddresses.append(shippingAddress)
            return True
        return False