class CacheProvider:
    def __init__(self, eviction_policy, storage):
        self.eviction_policy = eviction_policy
        self.storage = storage

    def set(self, key, value):
        try:
            self.storage.add(key, value)
            self.eviction_policy.key_accessed(key)
        except Exception:
            key_to_remove = self.eviction_policy.evict_key()
            if key_to_remove is None:
                raise RuntimeError("Unexpected State.")

            self.storage.remove(key_to_remove)
            self.set(key, value)

    def get(self, key):
        value = self.storage.get(key)
        self.eviction_policy.key_accessed(key)
        return value

    def get_current_usage(self):
        return self.storage.get_current_usage()
