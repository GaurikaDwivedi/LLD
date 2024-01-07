class Page:
    def __init__(self, pageId, name, description, creator):
        self._posts = None

        self._pageId = pageId
        self._name = name
        self._description = description
        self._creator = creator
        self._followers = set()

    def getCreator(self):
        return self._creator

    def updateDescription(self, description):
        self._description = description

    def updatePageName(self, name):
        self._name = name

    def getPageId(self):
        return self._pageId

    def getPageName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getFollowers(self):
        return self._followers

    def getPosts(self):
        return self._posts

    def addPost(self, post):
        self._posts.add(post)