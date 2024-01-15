class ProductReview:
    def __init__(self, reviewId, rating, review, product, reviewer):
        self._reviewId = reviewId
        self._rating = rating
        self._review = review
        self._product = product
        self._reviewer = reviewer

    def getRating(self):
        return self._rating

    def setRating(self, rating):
        self._rating = rating

    def getReview(self):
        return self._review

    def setReview(self, review):
        self._review = review

    def getProduct(self):
        return self._product

    def setProduct(self, product):
        self._product = product

    def getReviewer(self):
        return self._reviewer

    def setReviewer(self, reviewer):
        self._reviewer = reviewer