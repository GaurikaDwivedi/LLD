from Model.StatsResponse import *
from statistics import mean

class CacheService:
    def __init__(self, multi_level_cache, last_count):
        self.multi_level_cache = multi_level_cache
        self.last_count = last_count
        self.last_read_times = []
        self.last_write_times = []

    def set(self, key, value):
        write_response = self.multi_level_cache.set(key, value)
        self._add_times(self.last_write_times, write_response.time_taken)
        return write_response

    def get(self, key):
        read_response = self.multi_level_cache.get(key)
        self._add_times(self.last_read_times, read_response.total_time)
        return read_response

    def stats(self):
        avg_read_time = self._get_avg_time(self.last_read_times)
        avg_write_time = self._get_avg_time(self.last_write_times)
        usages = self.multi_level_cache.get_usages()
        return StatsResponse(avg_read_time, avg_write_time, usages)

    def _add_times(self, times, time):
        if len(times) == self.last_count:
            times.pop(0)
        times.append(time)

    def _get_avg_time(self, times):
        if not times:
            return 0.0
        return mean(times)
