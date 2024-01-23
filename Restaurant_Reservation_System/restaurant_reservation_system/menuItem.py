class MenuItem:
    def __init__(self, menuItemID, title, description, price):
        self._menuItemID = menuItemID
        self._title = title
        self._description = description
        self._price = price

    def updatePrice(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def getMenuItemID(self):
        return self._menuItemID

    def setMenuItemID(self, menuItemID):
        self._menuItemID = menuItemID

    def getTitle(self):
        return self._title

    def updateTitle(self, title):
        self._title = title

    def getDescription(self):
        return self._description

    def updateDescription(self, description):
        self._description = description
    
    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != MenuItem:
            return False
        menuItem = o
        if self._menuItemID != menuItem._menuItemID:
            return False
        if (self._title != menuItem._title) if self._title is not None else menuItem._title is not None:
            return False
        return self._description == menuItem._description if self._description is not None else menuItem._description is None

    def hashCode(self):
        result = self._menuItemID
        result = 31 * result + (hash(self._title) if self._title is not None else 0)
        result = 31 * result + (hash(self._description) if self._description is not None else 0)
        return result
