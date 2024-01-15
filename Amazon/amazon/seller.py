from .registeredUser import RegisteredUser
class Seller(RegisteredUser):
    def __init__(self, id, name, email, phone, location):
        self._products = None

        super().__init__(id, name, email, phone)
        self._location = location

    def addProduct(self, product):
        self._products.append(product)

    def fulfillOrder(self, order):
        # fulfill order
        pass

    def processRefund(self, order):
        return order.refund()

    def updateProductName(self, product, newName):
        if product in self._products:
            product.setName(newName)
            return True
        return False

    def updateProductDescription(self, product, newDescription):
        if product in self._products:
            product.setDescription(newDescription)
            return True
        return False
    
    def updateProductPrice(self, product, newPrice):
        if product in self._products:
            product.updatePrice(newPrice)
            return True
        return False

    def updateProductCategory(self, product, newCategory):
        if product in self._products:
            product.setCategory(newCategory)
            return True
        return False

    def sell(self, product):
        return product.sell()
