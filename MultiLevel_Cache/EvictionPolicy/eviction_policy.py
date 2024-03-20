from abc import ABC, abstractmethod

class EvictionPolicy(ABC):
    @abstractmethod
    def key_accessed(self, key):
        """
        Method to indicate that the given key has been accessed.
        """
        pass

    @abstractmethod
    def evict_key(self):
        """
        Method to evict a key from the eviction policy and return it.
        """
        pass
