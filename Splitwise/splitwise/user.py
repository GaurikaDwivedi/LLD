class User:
    def __init__(self, name):
        self.name = name
    
    def updateName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name