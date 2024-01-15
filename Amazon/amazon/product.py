class Product:
    def __init__(self, productID, name, description, price, category, availableItemCount, seller):
        self._productID = productID
        self._name = name
        self._description = description
        self._price = price
        self._category = category
        self._availableItemCount = availableItemCount
        self._seller = seller
        self._reviews = []

    def addReview(self, review):
        self._reviews.append(review)

    def getReview(self):
        for review in self._reviews:
            print(f"Reviews:\nCustomer Name: {review.getReviewer().getName()}\n"
                  f"Review: {review.getReview()}\n"
                  f"Rating: {review.getRating()}\n")

    def getAvailableCount(self):
        return self._availableItemCount

    def updatePrice(self, newPrice):
        self._price = newPrice

    def getPrice(self):
        return self._price

    def sell(self):
        if self._availableItemCount > 0:
            self._availableItemCount -= 1
            return True
        return False

    def getProductID(self):
        return self._productID

    def setProductID(self, productID):
        self._productID = productID

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getCategory(self):
        return self._category

    def setCategory(self, category):
        self._category = category
    
    def setAvailableItemCount(self, availableItemCount):
        self._availableItemCount = availableItemCount

    def getSeller(self):
        return self._seller

    def setSeller(self, seller):
        self._seller = seller