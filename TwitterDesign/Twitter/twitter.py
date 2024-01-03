from Twitter.user import User
from Twitter.userTweet import UserTweet
import heapq

class Twitter:
    counter = 0
    def __init__(self):
        Twitter.counter = 0
        self.useridToUserobject = {} # we need this map because in follow() and unfollow() methods 
                    # we pass userId and not User object, so we need a mapping between user id and corresponding user object

    def __exists(self,userId):
        return userId in self.useridToUserobject

    #Compose a new tweet.
    def postTweet(self,userId,tweetId):
        if not self.__exists(userId): #if this is the first call to this user, then create the user first
            self.useridToUserobject[userId] = User(userId)
        Twitter.counter += 1 #increment timestamp
        tweet = UserTweet(tweetId,Twitter.counter)
        user = self.useridToUserobject[userId]
        if user.getMostRecentTweet() is None:
            user.setMostRecentTweet(tweet) #this is going to be the first tweet of the user
        else:
            previousHead = user.getMostRecentTweet()
            newHead = tweet
            user.setMostRecentTweet(newHead)
            newHead.setNext(previousHead)

    # Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself.
    # Tweets must be ordered from most recent to least recent.
    def getNewsFeed(self, userId):
        res = []
        if not self.__exists(userId):
            return res
        min_heap = []  # min heap to store UserTweet objects
        visited = set()
        
        def add_tweet_to_heap(user):
            most_recent_tweet = user.getMostRecentTweet()
            if most_recent_tweet and most_recent_tweet.getTweetId() not in visited:
                heapq.heappush(min_heap, (-most_recent_tweet.getTimestamp(), most_recent_tweet))
                visited.add(most_recent_tweet.getTweetId())

        current_user = self.useridToUserobject[userId]
        for followee in current_user.getFollowees():
            followee_ = self.useridToUserobject[followee]
            if followee_.getMostRecentTweet():
                min_heap.append(followee_.getMostRecentTweet())

        while len(res) < 10 and min_heap:
            most_recent_tweet = heapq.heappop(min_heap)
            tweet_id = most_recent_tweet.getTweetId()
            res.append(tweet_id)

            next_tweet = most_recent_tweet.getNext()
            if next_tweet:
                add_tweet_to_heap(next_tweet)

        return res

    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    def follow(self,followerId,followeeId):
        if not self.__exists(followerId): # create the user if it is not created yet
            self.useridToUserobject[followerId] = User(followerId)
        if not self.__exists(followeeId): # create the user if it is not created yet
            self.useridToUserobject[followeeId] = User(followeeId)
        follower = self.useridToUserobject[followerId]
        followee = self.useridToUserobject[followeeId]
        follower.follow(followee)

    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    def unfollow(self,followerId,followeeId):
        if not self.__exists(followerId):  # create the user if it is not created yet
            self.useridToUserobject[followerId] = User(followerId)
        if not self.__exists(followeeId):  # create the user if it is not created yet
            self.useridToUserobject[followeeId] = User(followeeId)
        follower = self.useridToUserobject[followerId]
        followee = self.useridToUserobject[followeeId]
        follower.unfollow(followee)