import math
from multiprocessing import RLock

class MyCircularQueue:
    def __init__(self, k):
        self._lock = RLock()

        self.arr = [0 for _ in range(k)]
        self.head = 0
        self.itemCount = 0
        self.capacity = k

    def enQueue(self, value):
        self._lock.acquire()
        try:
            if self.isFull():
                return False
            self.itemCount += 1

            tail = int(math.fmod((self.head + self.itemCount - 1), self.capacity))
            self.arr[tail] = value
        finally:
            self._lock.release()
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.itemCount -= 1

        if self.head == self.capacity - 1:
            self.head = 0
        else:
            self.head = int(math.fmod((self.head + 1), self.capacity))
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        tail = int(math.fmod((self.head + self.itemCount - 1), self.capacity))
        return self.arr[tail]

    def isEmpty(self):
        return self.itemCount == 0

    def isFull(self):
        return self.itemCount == self.capacity
    
    def display(self):
     
        # condition for empty queue
        tail = int(math.fmod((self.head + self.itemCount - 1), self.capacity))
        if(self.head == -1): 
            print ("Queue is Empty")
        
        elif (tail >= self.head):
            print("Elements in the circular queue are:", 
                                              end = " ")
            for i in range(self.head, tail + 1):
                print(self.arr[i], end = " ")
            print ()
 
        else:
            print ("Elements in Circular Queue are:", 
                                           end = " ")
            for i in range(self.head, self.capacity):
                print(self.arr[i], end = " ")
            for i in range(0, tail + 1):
                print(self.arr[i], end = " ")
            print ()
 
        if ((tail + 1) % self.capacity == self.head):
            print("Queue is Full")
    
ob = MyCircularQueue(5)
ob.enQueue(14)
ob.enQueue(22)
ob.enQueue(13)
ob.enQueue(-6)
ob.display()
print ("Deleted value = ", ob.deQueue())
print ("Deleted value = ", ob.deQueue())
ob.display()
ob.enQueue(9)
ob.enQueue(20)
ob.enQueue(5)
ob.display()