class Message:
    def __init__(self, messageId, messageBody, creator):
        self._messageId = messageId
        self._creator = creator
        self._messageBody = messageBody
        self._recipients = set()
        self._media = set()

    def addMember(self, member):
        self._recipients.add(member)
        insert = None

    def setRecipients(self, recipients):
        self._recipients = recipients

    def leaveChat(self, member):
        if self._recipients.contains(member):
            self._recipients.remove(member)
            member.getMessages().remove(self)
            return True
        return False

    def send(self):
        self._creator.getMessages().add(self)
        for recipient in self._recipients:
            recipient.getMessages().add(self)

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Message:
            return False
        message = o
        return self._messageId == message._messageId

    def hashCode(self):
        return hash(self._messageId)