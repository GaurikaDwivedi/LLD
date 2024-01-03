class UserTweet:
    def __init__(self, tweetId, timestamp):
        self._next = None  # pointer to chronologically next tweet
        self._tweetId = tweetId
        self._timestamp = timestamp

    def getTimestamp(self):
        return self._timestamp

    def getTweetId(self):
        return self._tweetId

    def getNext(self):
        return self._next

    def setNext(self, nextTweet):
        self._next = nextTweet