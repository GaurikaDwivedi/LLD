from .storage import *
class InMemoryStorage(Storage):
    def __init__(self, capacity):
        self.storage = {}
        self.capacity = capacity

    def add(self, key, value):
        if self.is_storage_full():
            raise Exception("Storage is full.")
        self.storage[key] = value

    def get(self, key):
        return self.storage.get(key)

    def remove(self, key):
        if key in self.storage:
            del self.storage[key]

    def get_current_usage(self):
        return len(self.storage) / self.capacity

    def is_storage_full(self):
        return len(self.storage) == self.capacity