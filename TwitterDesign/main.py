from Twitter.twitter import Twitter

twitter = Twitter()
twitter.postTweet(1, 5)
print("User 1's news feed:", twitter.getNewsFeed(1)) 
#twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print("User 1's news feed:",twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print("User 1's news feed:",twitter.getNewsFeed(1))