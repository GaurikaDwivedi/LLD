from stackOverflow.AccountStatus import AccountStatus
class Member:

    def __init__(self, id):
        self._id = 0
        self._accountStatus = 0
        self._name = None
        self._displayName = None
        self._email = None
        self._reputation = 0
        self._isModerator = False
        self._isAdmin = False

        self._accountStatus = AccountStatus.ACTIVE

    def closeAccount(self):
        self._accountStatus = AccountStatus.CLOSED

    def cancelAccount(self):
        self._accountStatus = AccountStatus.CANCELED

    def blacklist(self):
        self._accountStatus = AccountStatus.BLACKLISTED

    def block(self):
        self._accountStatus = AccountStatus.BLOCKED

    def blockMember(self, member):
        if self._isAdmin:
            member.block()
        return False

    def unblockMember(self, member):
        if self._isAdmin:
            member._accountStatus = AccountStatus.ACTIVE
        return False

    def closeQuestion(self, question):
        if self._isAdmin or self._isModerator or self._id == question.getCreator().getId():
            question.close()
        return False

    def promoteToAdmin(self):
        self._isAdmin = True

    def promoteToModerator(self):
        self._isModerator = True

    def giveBountyTo(self, bountyReputation, receiver):
        if bountyReputation <= self._reputation and self._id != receiver._id:
            self._reputation -= bountyReputation
            receiver.receiveBounty(bountyReputation)
        return False

    def receiveBounty(self, bountyReputation):
        self._reputation += bountyReputation

    def getReputation(self):
        return self._reputation

    def getId(self):
        return self._id

    def getStatus(self):
        return self._accountStatus

    def getName(self):
        return self._name

    def getDisplayName(self):
        return self._displayName

    def getEmail(self):
        return self._email