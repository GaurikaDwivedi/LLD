from Model.WriteResponse import *
from Model.ReadResponse import *
from .ILevelCache import *

class DefaultLevelCache(ILevelCache):
    def __init__(self, level_cache_data, cache_provider, next_cache):
        self.level_cache_data = level_cache_data
        self.cache_provider = cache_provider
        self.next_cache = next_cache

    def set(self, key, value):
        cur_time = 0.0
        cur_level_value = self.cache_provider.get(key)
        cur_time += self.level_cache_data.read_time

        if value != cur_level_value:
            self.cache_provider.set(key, value)
            cur_time += self.level_cache_data.write_time

        next_response = self.next_cache.set(key, value)
        cur_time += next_response.time_taken

        return WriteResponse(cur_time)

    def get(self, key):
        cur_time = 0.0
        cur_level_value = self.cache_provider.get(key)
        cur_time += self.level_cache_data.read_time

        if cur_level_value is None:
            next_response = self.next_cache.get(key)
            cur_time += next_response.total_time
            cur_level_value = next_response.value

            if cur_level_value is not None:
                self.cache_provider.set(key, cur_level_value)
                cur_time += self.level_cache_data.write_time

        return ReadResponse(cur_level_value, cur_time)

    def get_usages(self):
        usages = []
        if self.next_cache is not None:
            usages = self.next_cache.get_usages()

        usages.insert(0, self.cache_provider.get_current_usage())
        return usages