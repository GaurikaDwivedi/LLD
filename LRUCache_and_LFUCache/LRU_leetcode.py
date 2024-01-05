class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

"""
# Create an instance of LRUCache with a capacity of 2
lru_cache = LRUCache(2)

# Set values for keys 1 and 2
lru_cache.set(1, 1)
lru_cache.set(2, 2)

# Get values for keys 1 and 2 (cache hit)
print(f"Value for key 1: {lru_cache.get(1)}")  # Output: Value for key 1: 1

# Set value for key 3 (causing eviction as capacity is 2)
lru_cache.set(3, 3)

# Get values for keys 2 and 3 (cache hit and miss)
print(f"Value for key 2: {lru_cache.get(2)}")  # Output: Value for key 2: -1 (key 2 is evicted)
print(f"Value for key 3: {lru_cache.get(3)}")  # Output: Value for key 3: 3

# Set values for keys 4 and 5 (causing eviction as capacity is 2)
lru_cache.set(4, 4)
lru_cache.set(5, 5)

# Get values for keys 1, 3, 4, and 5 (cache miss for key 1, hit for others)
print(f"Value for key 1: {lru_cache.get(1)}")  # Output: Value for key 1: -1 (key 1 is evicted)
print(f"Value for key 3: {lru_cache.get(3)}")  # Output: Value for key 3: -1
print(f"Value for key 4: {lru_cache.get(4)}")  # Output: Value for key 4: 4
print(f"Value for key 5: {lru_cache.get(5)}")  # Output: Value for key 5: 5
"""

lru_cache = LRUCache(3)
lru_cache.set(1, 1)
print(lru_cache.get(1))  # Output: Page 1 t

# Insert for pages 2, 3, and 4
lru_cache.set(2, 2)
lru_cache.set(3, 3)
lru_cache.set(4, 4)

# Get  for pages 1, 2, 3, and 4
print(lru_cache.get(1))  # Output: -1
print(lru_cache.get(2))  # Output: 2
print(lru_cache.get(3))  # Output: 3 
print(lru_cache.get(4))  # Output: 4 

# Insert  for page 5 (evicts page 2)
lru_cache.set(5, 5)

# Get for pages 2, 3, 4, and 5
print(lru_cache.get(2))  # Output:-1
print(lru_cache.get(3))  # Output:  3 
print(lru_cache.get(4))  # Output:  4 
print(lru_cache.get(5))  # Output:  5 