import time

from stackOverflow.Status import Status


class TextPhotoBasedEntity:
    def __init__(self, id, creator, text, photos):
        self.id = 0
        self.text = None
        self.creationDateTime = 0
        self.lastUpdated = 0
        self.creator = None
        self.photos = None
        self.membersWhoDownvotedThisEntity = None
        self.membersWhoUpvotedThisEntity = None
        self.numberOfUsersReportedThisEntity = 0
        self.status = None

        self.id = id
        self.status = Status.DEFAULT
        self.creator = creator
        self.text = text
        photos = []
        if photos is not None:
            self.photos = photos
        self.membersWhoDownvotedThisEntity = set()
        self.membersWhoUpvotedThisEntity = set()
        self.creationDateTime = round(time.time() * 1000)
        self.lastUpdated = round(time.time() * 1000)
        self.numberOfUsersReportedThisEntity = 0

    def equals(self, that):
        if isinstance(that, TextPhotoBasedEntity):
            return self.id == (that).id
        return False

    def upVote(self, memberId):
        if not self.membersWhoUpvotedThisEntity.contains(memberId):
            if self.membersWhoDownvotedThisEntity.contains(memberId):
                self.membersWhoDownvotedThisEntity.remove(memberId)
            else:
                self.membersWhoUpvotedThisEntity.add(memberId)

    def downVote(self, memberId):
        if not self.membersWhoDownvotedThisEntity.contains(memberId):
            if self.membersWhoUpvotedThisEntity.contains(memberId):
                self.membersWhoUpvotedThisEntity.remove(memberId)
            else:
                self.membersWhoDownvotedThisEntity.add(memberId)

    def report(self):
        self.numberOfUsersReportedThisEntity += 1

    def updateText(self, text):
        self.text = text
        self.lastUpdated = round(time.time() * 1000)

    def removePhoto(self, photosToBeDeleted):
        self.photos.removeAll(photosToBeDeleted)
        self.lastUpdated = round(time.time() * 1000)

    def addPhotos(self, newPhotosToBeAdded):
        self.photos.extend(newPhotosToBeAdded)
        self.lastUpdated = round(time.time() * 1000)

    def getUpvoteCount(self):
        return self.membersWhoUpvotedThisEntity.size()

    def getDownvoteCount(self):
        return self.membersWhoDownvotedThisEntity.size()

    def getCreator(self):
        return self.creator

    def delete(self):
        self.status = Status.DELETED

    def getId(self):
        return self.id

    def getText(self):
        return self.text

    def getCreationDateTime(self):
        return self.creationDateTime

    def getLastUpdated(self):
        return self.lastUpdated

    def getPhotos(self):
        return self.photos

    def getMembersWhoDownvotedThisEntity(self):
        return self.membersWhoDownvotedThisEntity

    def getMembersWhoUpvotedThisEntity(self):
        return self.membersWhoUpvotedThisEntity

    def getVoteCount(self):
        return self.getUpvoteCount() - self.getDownvoteCount()

    def getNumberOfUsersReportedThisEntity(self):
        return self.numberOfUsersReportedThisEntity

    def getStatus(self):
        return self.status