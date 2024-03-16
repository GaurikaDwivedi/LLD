from .storage import *

class HashMapBasedStorage(Storage):
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}

    def add(self, key, value):
        if self.is_storage_full():
            raise Exception("Capacity Full.....")
        self.storage[key] = value

    def remove(self, key):
        if key not in self.storage:
            raise Exception(f"{key} doesn't exist in cache.")
        del self.storage[key]

    def get(self, key):
        if key not in self.storage:
            raise Exception(f"{key} doesn't exist in cache.")
        return self.storage[key]

    def is_storage_full(self):
        return len(self.storage) == self.capacity

    def display(self):
        print(self.storage)