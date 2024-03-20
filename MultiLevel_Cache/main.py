from Service.CacheService import CacheService
from Provider.CacheProvider import CacheProvider
from Provider.DefaultLevelCache import DefaultLevelCache
from Provider.NullEffectLevelCache import NullEffectLevelCache
from Model.LevelCacheData import LevelCacheData
from EvictionPolicy.lru import LRUEvictionPolicy
from Storage.InMemoryStorage import InMemoryStorage

def main():

    # create 2 cache_provider because each level will be needing a cache. So just created caches with some capacity
    c1 = create_cache(capacity=10)
    c2 = create_cache(capacity=20)

    # create actual level_cache, here l1_cache is Level-1 cache which further points to l2_cache(last cache hence points to Null)
    # cl1 & cl2 is levelCache data, read_time & write_time of respective level
    cl1 = LevelCacheData(read_time=1, write_time=3)
    cl2 = LevelCacheData(read_time=2, write_time=4)

    l2_cache = DefaultLevelCache(cl2, c2, NullEffectLevelCache())
    l1_cache = DefaultLevelCache(cl1, c1, l2_cache)

    # cache_service points to level-1
    cache_service = CacheService(l1_cache, last_count=5)

    """
    Try to set 2 values in cache. It first checks if particular level has this key, as this is new key so it'll not be present in any of the levels.
    so, it'll write it at all levels. To do all of this, total_time = read at both levels + write at both levels = 10
    """
    w1 = cache_service.set("k1", "v1")
    w2 = cache_service.set("k2", "v2")

    assert w1.time_taken == 10
    assert w2.time_taken == 10

    """
    When we try to read value, all levels have this, so we get it from L1 itself, hence read_time = 1.
    """
    r1 = cache_service.get("k1")
    assert r1.value == "v1"
    assert r1.total_time == 1

    r2 = cache_service.get("k2")
    assert r2.value == "v2"
    assert r2.total_time == 1

    # Explicitly remove key from l1 for testing.
    c1.set("k1", None)

    """
    As we have removed it from L1, it's not present in L1. But it's there in L2. So, it'll read at L1(time=1), then read at L2(time=2)
    and then write at L1(time=3). hence total_time=6.
    """

    r1_after_removal_from_l1 = cache_service.get("k1")
    assert r1_after_removal_from_l1.value == "v1"
    assert r1_after_removal_from_l1.total_time == 6

    # Since we have written value at previous step when it wasn't found while reading, so value is now present at L1, so read_time = read time of L1. 
    re_read = cache_service.get("k1")
    assert re_read.value == "v1"
    assert re_read.total_time == 1

    # Since value is present at both level, it reads at L1(time=1), value present, no need to write; it reads at L2(time=2), value present, no need to write
    # total time = 1+2 = 3
    re_writing_value = cache_service.set("k1", "v1")
    assert re_writing_value.time_taken == 3

def create_cache(capacity):
    return CacheProvider(LRUEvictionPolicy(), InMemoryStorage(capacity))

if __name__ == "__main__":
    main()
