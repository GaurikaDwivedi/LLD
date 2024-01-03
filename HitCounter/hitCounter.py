import math


class HitCounter:
    def __init__(self):
        self._timestamp = [0 for _ in range(300)]
        self._hits = [0 for _ in range(300)]

    def hit(self, time): # time - The current time (in seconds granularity)
        index = int(math.fmod(time, 300))
        if self._timestamp[index] != time:
            self._timestamp[index] = time
            self._hits[index] = 1
        else:
            self._hits[index] += 1

    def getHits(self, time):    # time - The current time (in seconds granularity)
        total = 0
        for i in range(0, 300): 
            if time - self._timestamp[i] < 300: # take value of hits[i] only if hits[i] was populated in last 300 seconds.
                                    # If hit() was not called for a certain timestamp in last
                                    # 300 seconds then we do not count them. This is important because for
                                    # timestamp > 300 hits[timestamp] could still be non-zero even if there was no hit for that specific
                                    # timestamp due to using mod and thereby reuse the indices.
                total += self._hits[i]
        return total