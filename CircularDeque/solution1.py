import math

class CircularDeque:

    def __init__(self):

        self.arr = []
        self.head = 0
        self.tail = 0
        self.capacity = 0
        self.count = 0

    def MyCircularDeque(self, k):
        self.arr = [0 for _ in range(k)]
        self.head = 0
        self.tail = 0
        self.count = 0
        self.capacity = k

    def _decrement(self, index):
        if index == 0:
            return self.capacity - 1
        return int(math.fmod((index - 1), self.capacity))

    def _increment(self, index):

        if index == self.capacity - 1:
            return 0
        return int(math.fmod((index + 1), self.capacity))

    def insertFront(self, value):
        if self.count == self.capacity:
            return False
        self.count += 1
        if self.count == 1:
            self.head = 0
            self.tail = 0
            self.arr[0] = value
            return True
        self.head = self._decrement(self.head)
        self.arr[self.head] = value
        return True

    def insertLast(self, value):
        if self.count == self.capacity:
            return False
        self.count += 1
        if self.count == 1:
            self.head = 0
            self.tail = 0
            self.arr[0] = value
            return True
        self.tail = self._increment(self.tail)
        self.arr[self.tail] = value
        return True

    def deleteFront(self):
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = 0
            self.tail = 0
        self.head = self._increment(self.head)
        self.count -= 1
        return True

    def deleteLast(self):
        if self.count == 0:
            return False
        if self.count == 1:
            self.head = 0
            self.tail = 0
        self.tail = self._decrement(self.tail)
        self.count -= 1
        return True

    def getFront(self):
        if self.count == 0:
            return -1
        return self.arr[self.head]

    def getRear(self):
        if self.count == 0:
            return -1
        return self.arr[self.tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity
    