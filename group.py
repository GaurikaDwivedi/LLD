from splitwise.user import User
from splitwise.split import Split

class Group:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.splits = {}
    
    def addUser(self, userId):
        self.users[userId] = User(userId)
    
    def removeUser(self, userId):
        del self.users[userId]
    
    def addSplit(self, paidBy, paidTo, amounts):
        if(paidBy in self.splits):
            self.splits[paidBy]
        else:
            self.splits[paidBy] = Split()
            self.splits[paidBy].setPaidByUser(paidBy)
            for i in range(0, len(paidTo)):
                self.splits[paidBy].setPaidToUser(paidTo[i], amounts[i])
    
    def showAllUsers(self):
        for user in self.users:
            self.showUser(user)

    def showUser(self, userId):
        if(userId not in self.users):
            print("user does not exist in group")
            return 
        else:
            Flag = False
            for paidByUser in self.splits:
                if(userId in self.splits[paidByUser]):
                    if(userId in self.splits and paidByUser in self.splits[userId]):
                        amt = self.splits[paidByUser][userId] - self.splits[userId][paidByUser]
                        if(amt > 0):
                            Flag = True
                            print(self.users[userId].name + " Owes " + self.users[paidByUser].name + " : " + str(amt))
                    else:
                        Flag = True
                        print(self.users[userId].name + " Owes " + self.users[paidByUser].name + " : " + str(self.splits[paidByUser][userId]))
            if(not Flag):
                print("No balances for " + userId)
    
    def addExpense(self, paidBy, paidTo, amounts):
        if(paidBy not in self.splits):
            self.splits[paidBy] = {} 
        for i in range(0, len(paidTo)):
            if(paidTo[i] != paidBy):
                if(paidTo[i] not in self.splits[paidBy]):
                    self.splits[paidBy][paidTo[i]] = 0
                self.splits[paidBy][paidTo[i]] += amounts[i]
        self.showAllUsers()
    
    def addExpenseByPercentSplit(self, paidBy, paidTo, percents, totalAmount):
        amounts = [] 
        for percent in percents:
            amt = percent*totalAmount/100
            amounts.append(amt)
        self.addExpense(paidBy, paidTo, amounts)
    
    def addExpenseByEqualSplit(self, paidBy, paidTo, totalAmount):
        amounts = []
        users = len(paidTo)
        for user in paidTo:
            amounts.append(totalAmount/users)
        self.addExpense(paidBy, paidTo, amounts)
    
    def addExpenseByExactSplit(self, paidBy, paidTo, amounts):
        self.addExpense(paidBy, paidTo, amounts)