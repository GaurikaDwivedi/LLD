import uuid
from .order import Order

class Cart:

    def __init__(self):
        self._customer = None
        self._productCounts = {}

    def addItem(self, item, quantity):
        if item in self._productCounts.keys():
            self._productCounts[item] = self._productCounts[item] + quantity
        else:
            self._productCounts[item] = quantity
            
    def removeItem(self, item):
        if(item in self._productCounts.keys()):
            self._productCounts.pop(item)
            return True
        return False
    
    def updateItemQuantity(self, item, newQuantity):
        if item in self._productCounts.keys():
            if newQuantity == 0:
                self.removeItem(item)
            self._productCounts[item] = self._productCounts[item] - 1
            return True
        return False
    
    def getItems(self):
        return self._productCounts
    
    def checkout(self):
        order_number = str(uuid.uuid4())
        products_ordered = list(self._productCounts.keys())
        
        # Check if there's enough stock for each product
        for product in products_ordered:
            if product.getAvailableCount() < self._productCounts[product]:
                print(f"Error: Insufficient stock for {product.getName()}. Checkout failed.")
                return None

        # If there's enough stock, proceed with creating the order
        for product in products_ordered:
            seller = product.getSeller() # get seller
            seller.sell(product) # sell product, decrease avaialble count

        order = Order(order_number, products_ordered)
        return order
    
    def clear(self):
        self._productCounts = {}