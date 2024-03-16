class Cache:

    def __init__(self, eviction_policy, storage):
        self.eviction_policy = eviction_policy
        self.storage = storage

    def put(self, key, value):
        try:
            self.storage.add(key, value)
            self.eviction_policy.key_accessed(key)
        except:
            print("Got storage full. Will try to evict.")
            key_to_remove = self.eviction_policy.evict_key()
            if key_to_remove is None:
                raise RuntimeError("Unexpected State. Storage full and no key to evict.")
            self.storage.remove(key_to_remove)
            print("Creating space by evicting item...", key_to_remove)
            self.put(key, value)

    def get(self, key):
        try:
            value = self.storage.get(key)
            self.eviction_policy.key_accessed(key)
            return value
        except:
            print("Tried to access non-existing key.")
            return None
