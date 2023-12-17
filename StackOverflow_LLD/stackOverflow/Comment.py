from stackOverflow.TextPhotoBasedEntity import TextPhotoBasedEntity


class Comment(TextPhotoBasedEntity):
    def __init__(self, id, commenter, text, photos):
        super().__init__(id, commenter, text, photos)