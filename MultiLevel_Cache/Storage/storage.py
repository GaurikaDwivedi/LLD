from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def add(self, key, value):
        """
        Method to add a key-value pair to the storage.
        """
        pass

    @abstractmethod
    def remove(self, key):
        """
        Method to remove a key from the storage.
        """
        pass

    @abstractmethod
    def get(self, key):
        """
        Method to retrieve the value associated with a key from the storage.
        """
        pass
    
    @abstractmethod
    def get_current_usage():
        pass