from movie_rental_system.comparable import Comparable

class Movie(Comparable):

    def __init__(self,id, shopId, price):
        self._id = id
        self._shopId = shopId
        self._price = price

    def equals(self, ob):
        if isinstance(ob, Movie):
            return self._id == (ob)._id and self._shopId == (ob)._shopId
        return False

    def compareTo(self, that):
        if self._price != that._price:
            return Comparable._compare(self._price, that._price)
        if self._shopId != that._shopId:
            return Comparable._compare(self._shopId, that._shopId)
        return Comparable._compare(self._id, that._id)
    
    def _cmpkey(self):
        # Ensure _cmpkey returns a tuple with the desired comparison order
        return (self._price, self._shopId, self._id)
    
    def __hash__(self):
        return hash((self._id, self._shopId))

    @property
    def id(self):
        return self._id
    
    def getShopId(self):
        return self._shopId