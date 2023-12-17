from stackOverflow.Status import Status
from stackOverflow.TextPhotoBasedEntity import TextPhotoBasedEntity


class Question(TextPhotoBasedEntity):
    def __init__(self, id, askingMember, title, text, photos, tags, bounty):
        self._title = None
        self._status = None
        self._bounty = None
        self._tags = None
        self._comments = None
        self._answers = None

        super().__init__(id, askingMember, text, photos)
        self._status = Status.OPEN
        self._title = title
        self._bounty = bounty
        if tags is not None:
            self._tags = tags
        else:
            self._tags = []
        self._comments = []
        self._answers = []

    def close(self):
        self._status = Status.CLOSED

    def addComment(self, newComment):
        self._comments.append(newComment)

    def addAnswer(self, newAnswer):
        self._answers.append(newAnswer)

    def getTitle(self):
        return self._title

    def getStatus(self):
        return self._status

    def getBounty(self):
        return self._bounty

    def getTags(self):
        return self._tags

    def getComments(self):
        return self._comments

    def getAnswers(self):
        return self._answers
    def receiveBounty(self, reputation, creator=None):
        if creator:
            creator.receiveBounty(reputation)
        else:
            # Handle the case where the creator is not specified
            pass
