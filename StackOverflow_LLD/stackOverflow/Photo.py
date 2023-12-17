import time


class Photo:
    def __init__(self, id, photoPath, creator):
        self._id = id
        self._photoPath = photoPath
        self._creationDate = round(time.time() * 1000)
        self._creatingMember = creator

    def equals(self, that):
        if isinstance(that, Photo):
            return self._id == (that)._id
        return False

    def getId(self):
        return self._id

    def getPhotoPath(self):
        return self._photoPath

    def getCreationDate(self):
        return self._creationDate

    def getCreatingMember(self):
        return self._creatingMember