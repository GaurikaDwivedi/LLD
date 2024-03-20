from abc import ABC, abstractmethod

class ILevelCache(ABC):
    @abstractmethod
    def set(self, key, value):
        """Set method to store a key-value pair."""
        pass

    @abstractmethod
    def get(self, key):
        """Get method to retrieve the value associated with a key."""
        pass

    @abstractmethod
    def get_usages(self):
        """Method to get the usages."""
        pass
