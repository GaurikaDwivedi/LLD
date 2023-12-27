from splitwise.user import User
from splitwise.group import Group

class System:
    def __init__(self):
        self.users = {}
        self.groups = {}
    
    def registerUser(self, name):
        self.users[name] = User(name)
    
    def delUser(self, userId):
        del self.users[userId]
    
    def registerGroup(self, groupName, users):
        newGroup = Group(groupName)
        for user in users:
            newGroup.addUser(user)
        self.groups[newGroup.name] = newGroup
    
    def getGroup(self, groupId):
        if(groupId in self.groups):
            return self.groups[groupId]
        print("No such group exists in system")
    
    def delGroup(self, groupId):
        del self.groups[groupId]