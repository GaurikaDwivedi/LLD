from Factories.cache_factory import *

lru_cache = CacheFactory().default_cache(3, policy='LRU')
lru_cache.put(1, 1)
print("Value for key 1", lru_cache.get(1))  # Output: Page 1 t

# Insert for pages 2, 3, and 4
lru_cache.put(2, 2)
lru_cache.put(3, 3)
lru_cache.put(4, 4)

# Get  for pages 1, 2, 3, and 4
print("Value for key 1",lru_cache.get(1))  # Output: -1
print("Value for key 2",lru_cache.get(2))  # Output: 2
print("Value for key 3",lru_cache.get(3))  # Output: 3 
print("Value for key 4",lru_cache.get(4))  # Output: 4 

# Insert  for page 5 (evicts page 2)
lru_cache.put(5, 5)

# Get for pages 2, 3, 4, and 5
print("Value for key 2",lru_cache.get(2))  # Output:-1
print("Value for key 3",lru_cache.get(3))  # Output:  3 
print("Value for key 4",lru_cache.get(4))  # Output:  4 
print("Value for key 5",lru_cache.get(5))  # Output:  5 



"""lfu_cache = CacheFactory().default_cache(3, policy='LFU')

# Insert values into the cache
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
lfu_cache.put(3, 3)
lfu_cache.put(4, 4)

# Get values from the cache
print("Value for key 4",lfu_cache.get(4))  # Output: 4
print("Value for key 3",lfu_cache.get(3))  # Output: 3
print("Value for key 2",lfu_cache.get(2))  # Output: 2
print("Value for key 1",lfu_cache.get(1)) 
# Insert a new value, evicting the least frequently used (1 in this case)
#print("Value for key 4",lfu_cache.get(4))  # Output: 4
#print("Value for key 3",lfu_cache.get(3))  # Output: 3
lfu_cache.put(5, 5)

# Get values from the cache
print("Value for key 1",lfu_cache.get(1))  # Output: -1 (1 was evicted)
print("Value for key 2",lfu_cache.get(2))  # Output: 2
print("Value for key 3",lfu_cache.get(3))  # Output: 3
print("Value for key 4",lfu_cache.get(4))  # Output: -1 (4 was evicted bcoz freq of all is same so evict as per least recently useed)
print("Value for key 5",lfu_cache.get(5))  # Output: 5
"""