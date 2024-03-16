from DLL_algo.dll import * 
from .eviction_policy import *

class LRUEvictionPolicy(EvictionPolicy):
    
    def __init__(self):
        self.dll = DLinkedList(0)
        self.mapper = {}

    def key_accessed(self, key):
        if key in self.mapper:
            node = self.mapper[key]
            self.dll.detach_node(node)
            self.dll.add_node_at_last(node)
        else:
            new_node = self.dll.add_element_at_last(key)
            self.mapper[key] = new_node

    def evict_key(self):
        first = self.dll.get_first_node()
        if first is None:
            return None
        self.dll.detach_node(first)
        del self.mapper[first.key]
        return first.value
