import time

class TextAndPhotoBasedContent:
    def __init__(self, contentId, text, blobUrlsForPhotos, creator):
        self._membersWhoLikedThisContent = []
        self._contentId = contentId
        self._text = text
        self._blobUrlsForPhotos = blobUrlsForPhotos
        self._creator = creator
        self._creationDateTime = round(time.time() * 1000)

    def likedBy(self, member):
        if member not in self._membersWhoLikedThisContent:
            self._membersWhoLikedThisContent.append(member)
            return True
        return False

    def undoLikeBy(self, member):
        if member in self._membersWhoLikedThisContent:
            self._membersWhoLikedThisContent.remove(member)
            return True
        return False

    def getTotalLikes(self):
        return len(self._membersWhoLikedThisContent)

    def getContentId(self):
        return self._contentId

    def getText(self):
        return self._text

    def updateText(self, text):
        self._text = text

    def getCreator(self):
        return self._creator

    def getBlobUrlsForPhotos(self):
        return self._blobUrlsForPhotos

    def setBlobUrlsForPhotos(self, blobUrlsForPhotos):
        self._blobUrlsForPhotos = blobUrlsForPhotos

    def deletePhoto(self, blobUrlForPhotoToBeDeleted):
        if self._blobUrlsForPhotos.contains(blobUrlForPhotoToBeDeleted):
            self._blobUrlsForPhotos.remove(blobUrlForPhotoToBeDeleted)
            return True
        return False

    def addPhoto(self, blobUrlForPhotoToBeAdded):
        if not self._blobUrlsForPhotos.contains(blobUrlForPhotoToBeAdded):
            self._blobUrlsForPhotos.add(blobUrlForPhotoToBeAdded)
            return True
        return False

    def getCreationDateTime(self):
        return self._creationDateTime