class Node:
    pageNumber = None
    pageContent = None
    prev = None
    next = None

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.map = {}
        self.head = None
        self.tail = None

    def getContent(self, pageNumber):
        if pageNumber in self.map:
            node = self.map[pageNumber]
            self.__remove(node)
            self.__attachFront(node)
            return node.pageContent
        return None

    def insertContent(self, pageNumber, pageContent):
        if pageNumber in self.map:
            node = self.map[pageNumber]
            node.pageContent = pageContent
            self.__remove(node)
            self.__attachFront(node)
            self.map[pageNumber] = node
            return
        self.count += 1
        node = Node()
        node.pageNumber = pageNumber
        node.pageContent = pageContent
        self.__attachFront(node)
        self.map[pageNumber] = node

        if self.count > self.size:
            del self.map[self.tail.pageNumber]
            self.__remove(self.tail)
            self.count -= 1

    def __remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next  # Update the head to the next node

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # Update the tail to the previous node

    def __attachFront(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

# Create an instance of LRUCache with a size of 3
lru_cache = LRUCache(3)

# Insert content for page 1
lru_cache.insertContent(1, "Page 1 Content")
print(lru_cache.getContent(1))  # Output: Page 1 Content

# Insert content for pages 2, 3, and 4
lru_cache.insertContent(2, "Page 2 Content")
lru_cache.insertContent(3, "Page 3 Content")
lru_cache.insertContent(4, "Page 4 Content")

# Get content for pages 1, 2, 3, and 4
print(lru_cache.getContent(1))  # Output: Page 1 Content
print(lru_cache.getContent(2))  # Output: Page 2 Content
print(lru_cache.getContent(3))  # Output: Page 3 Content
print(lru_cache.getContent(4))  # Output: Page 4 Content

# Insert content for page 5 (evicts page 2)
lru_cache.insertContent(5, "Page 5 Content")

# Get content for pages 2, 3, 4, and 5
print(lru_cache.getContent(2))  # Output: None (page 2 was evicted)
print(lru_cache.getContent(3))  # Output: Page 3 Content
print(lru_cache.getContent(4))  # Output: Page 4 Content
print(lru_cache.getContent(5))  # Output: Page 5 Content
