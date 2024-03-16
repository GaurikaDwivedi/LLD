from EvictionPolicy.lru import *
from EvictionPolicy.lfu import *
from Storage.hash_map import *
from Cache.cache import *

class CacheFactory:
    def default_cache(self, capacity, policy='LRU'):
        if policy.upper() == 'LRU':
            return Cache(LRUEvictionPolicy(), HashMapBasedStorage(capacity))
        elif policy.upper() == 'LFU':
            return Cache(LFUEvictionPolicy(), HashMapBasedStorage(capacity))
        else:
            raise ValueError("Invalid policy. Supported policies: 'LRU', 'LFU'")
