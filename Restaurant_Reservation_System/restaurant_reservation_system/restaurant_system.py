class RestaurantManagementSystem:
    def __init__(self):
        self._clientCompanies = []

    def addNewClient(self, restaurant):
        if not restaurant in self._clientCompanies:
            self._clientCompanies.append(restaurant)

    def removeClient(self, restaurant):
        if restaurant in self._clientCompanies:
            self._clientCompanies.remove(restaurant)