class Group:
    def __init__(self, groupId, name, description, creator):
        self._groupId = 0
        self._name = None
        self._description = None
        self._members = set()
        self._admins = set()
        self._moderators = set()
        self._creator = None
        self._posts = set()
        self._bannedmembers = set()

        self._groupId = groupId
        self._name = name
        self._description = description
        self._creator = creator
        self._admins.add(creator)   
        self._members.add(creator)

    def getGroupId(self):
        return self._groupId

    def getName(self):
        return self._name

    def updateName(self, name):
        self._name = name

    def getDescription(self):
        return self._description

    def updateDescription(self, description):
        self._description = description

    def getMembers(self):
        return self._members

    def getAdmins(self):
        return self._admins

    def getBannedmembers(self):
        return self._bannedmembers

    def removeAdmin(self, admin):
        if admin in self._admins:
            self._moderators.remove(admin)
            return True
        return False

    def addAdmin(self, member):
        if member not in self._admins:
            self._admins.add(member)
            return True
        return False

    def getModerators(self):
        return self._moderators

    def removeModerator(self, moderator):
        if moderator in self._moderators:
            self._moderators.remove(moderator)
            return True
        return False

    def addModerator(self, member):
        if member not in self._moderators:
            self._moderators.add(member)
            return True
        return False

    def getCreator(self):
        return self._creator

    def getPosts(self):
        return self._posts

    def addPost(self, post):
        self._posts.add(post)

    def deletePost(self, post):
        if post in self._posts:
            self._posts.remove(post)
            return True
        return False