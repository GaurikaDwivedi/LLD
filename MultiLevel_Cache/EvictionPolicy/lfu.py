from collections import defaultdict
from DLL_algo.dll import * 
from .eviction_policy import *

class LFUEvictionPolicy(EvictionPolicy):

    def __init__(self):
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = defaultdict(lambda: DLinkedList(0))

    def _update(self, node):
        freq = node.freq
        self.freq_map[freq].detach_node(node)
        node.freq += 1
        self.freq_map[node.freq].add_node_at_head(node)

        while self.freq_map[self.min_freq].is_empty():
            self.min_freq += 1
        return node.value
    
    def key_accessed(self, key):
        if key in self.key_map:
            node = self.key_map[key]
            self._update(node)
        else:
            new_node = self.freq_map[0].add_element_at_head(key)
            self.key_map[key] = new_node

    def evict_key(self):
        old = self.freq_map[self.min_freq].pop()
        if old is None:
            return None
        del self.key_map[old.key]
        return old.value