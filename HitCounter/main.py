from hitCounter import HitCounter
hitCounter = HitCounter()
hitCounter.hit(1)      # hit at timestamp 1.
hitCounter.hit(2)     # hit at timestamp 2.
hitCounter.hit(3)      # hit at timestamp 3.
print(hitCounter.getHits(4))   # get hits at timestamp 4, return 3.

hitCounter.hit(300)     # hit at timestamp 300.

print(hitCounter.getHits(300)); # get hits at timestamp 300, return 4.

print(hitCounter.getHits(301)) # get hits at timestamp 301, return 3.