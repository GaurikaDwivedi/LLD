class Split:
    def __init__(self):
        self.paidBy = None # userId 
        self.paidTo = {} # userIds 
    
    def getPaidByUser(self):
        return self.paidBy
    
    def setPaidByUser(self, userId):
        self.paidBy = userId
    
    def getPaidToUsers(self, userId):
        return self.paidTo[userId]
    
    def setPaidToUser(self, userId, amount):
        if(userId not in self.paidTo):
            self.paidTo[userId] = 0
        self.paidTo[userId] += amount
    
    def removePaidToUser(self, userId):
        del self.paidTo[userId]