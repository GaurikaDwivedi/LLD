from .text_and_photo_based_content import TextAndPhotoBasedContent
class Post(TextAndPhotoBasedContent):
    def __init__(self, contentId, text, blobUrlsForPhotos, creator):
        self._totalShares = 0
        super().__init__(contentId, text, blobUrlsForPhotos, creator)

    def share(self):
        self._totalShares += 1

    def getTotalShares(self):
        return self._totalShares