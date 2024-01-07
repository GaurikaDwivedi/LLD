from .text_and_photo_based_content import TextAndPhotoBasedContent
class Comment(TextAndPhotoBasedContent):
    def __init__(self, contentId, text, blobUrlsForPhotos, creator):
        super().__init__(contentId, text, blobUrlsForPhotos, creator)