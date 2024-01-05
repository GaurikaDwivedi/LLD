import math

class CircularQueue:
    def __init__(self, k):
        self.arr = [0 for _ in range(k)]
        self.head = 0
        self.tail = -1
        self.itemCount = 0
        self.capacity = k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.itemCount += 1
        if self.tail == self.capacity - 1:
            self.tail = 0
        else:
            self.tail = int(math.fmod((self.tail + 1), self.capacity))
        self.arr[self.tail] = value
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
        return self.arr[self.tail]

    def isEmpty(self):
        return self.itemCount == 0

    def isFull(self):
        return self.itemCount == self.capacity
    
    def display(self):
     
        # condition for empty queue
        if(self.head == -1): 
            print ("Queue is Empty")
 
        elif (self.tail >= self.head):
            print("Elements in the circular queue are:", 
                                              end = " ")
            for i in range(self.head, self.tail + 1):
                print(self.arr[i], end = " ")
            print ()
 
        else:
            print ("Elements in Circular Queue are:", 
                                           end = " ")
            for i in range(self.head, self.capacity):
                print(self.arr[i], end = " ")
            for i in range(0, self.tail + 1):
                print(self.arr[i], end = " ")
            print ()
 
        if ((self.tail + 1) % self.capacity == self.head):
            print("Queue is Full")
    
ob = CircularQueue(5)
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