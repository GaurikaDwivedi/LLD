class Menu:
    def __init__(self):
        self._menuID = 0
        self._menuItems = []

    def addMenuItem(self, menuItem):
        if not menuItem in self._menuItems:
            self._menuItems.append(menuItem)

    def removeMenuItem(self, menuItem):
        if menuItem in self._menuItems:
            self._menuItems.remove(menuItem)

    def getAllMenuItems(self):
        return self._menuItems

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Menu:
            return False
        menu = o
        return self._menuID == menu._menuID

    def hashCode(self):
        return self._menuID
