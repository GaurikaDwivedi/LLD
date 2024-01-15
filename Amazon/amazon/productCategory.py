class ProductCategory:
    def __init__(self, categoryId, name, description):
        self._categoryId = categoryId
        self._name = name
        self._description = description

    def getName(self):
        return self._name

    def updateName(self, name):
        self._name = name

    def getCategoryId(self):
        return self._categoryId

    def getDescription(self):
        return self._description

    def updateDescription(self, description):
        self._description = description