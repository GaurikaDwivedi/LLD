import time

from stackOverflow.TextPhotoBasedEntity import TextPhotoBasedEntity


class Answer(TextPhotoBasedEntity):
    def __init__(self, id, creatingMember, text, photos):
        self._solvedProblem = False
        self._comments = None

        super().__init__(id, creatingMember, text, photos)
        self._comments = []

    def markAsASolution(self):
        self._solvedProblem = True

    def updateText(self, text):
        self.text = text
        lastUpdated = round(time.time() * 1000)

    def addComment(self, newComment):
        self._comments.append(newComment)

    def receiveBounty(self, reputation, creator=None):
        creator.receiveBounty(reputation)

    def isSolvedProblem(self):
        return self._solvedProblem

    def getComments(self):
        return self._comments