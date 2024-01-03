class User:
    def __init__(self, userId):
        self._userId = userId
        self._head = None # most recent tweet
        self._following = set() # list of users current user is following
                            # we are taking Set data structure because there would be no duplicate user ids
        self._following.add(self._userId)

    def unfollow(self, user):
        if user.getUserId() != self.getUserId(): # a user cannot unfollow himself / herself
            self._following.discard(user.getUserId())

    def follow(self, user):
        self._following.add(user.getUserId())

    def getFollowees(self):
        return self._following

    def getUserId(self):
        return self._userId

    def getMostRecentTweet(self):
        return self._head

    def setMostRecentTweet(self, tweet):
        self._head = tweet

