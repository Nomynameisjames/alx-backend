                Cache replacement policies

This are algorithms used in computer systems to decide which cache entries to remove when the cache is full and a new entry needs to be added.

Caches are used to store frequently accessed data and are much faster to access than the original source of data. However, caches have limited capacity,
so when the cache becomes full, some entries must be removed to make room for new ones.

Cache replacement policies determine which entry to remove from the cache when space is needed.
The goal of these policies is to remove the least important or least frequently accessed data, while keeping the most important or frequently accessed data in the cache.

    Some common cache replacement policies include:

1. Least Recently Used (LRU): This policy removes the least recently used entry from the cache. It assumes that if an entry has not been accessed recently,
it is less likely to be accessed in the future.

2. First In First Out (FIFO): This policy removes the oldest entry from the cache. It assumes that the oldest entry is the least valuable and should be removed first.

3. Least Frequently Used (LFU): This policy removes the least frequently used entry from the cache. It assumes that if an entry has been accessed less frequently than others,
it is less important and can be removed.

4. Random Replacement: This policy removes a randomly selected entry from the cache. It does not take into account how frequently or recently the entry was accessed.

5. Most Recently Used (MRU): This in contrast to Least Recently Used (LRU), MRU discards the most recently used items first.
MRU cache algorithms have more hits than LRU due to their tendency to retain older data.[9] MRU algorithms are most useful in situations where the older an item is,
the more likely it is to be accessed.

6. Least-frequently used (LFU): Counts how often an item is needed. Those that are used least often are discarded first.
This works very similar to LRU except that instead of storing the value of how recently a block was accessed,
we store the value of how many times it was accessed. So of course while running an access sequence we will replace a block which was used fewest times from our cache.
E.g., if A was used (accessed) 5 times and B was used 3 times and others C and D were used 10 times each, we will replace B.

The choice of cache replacement policy depends on the specific use case and the nature of the data being cached.
Some policies may be more effective than others depending on the access patterns of the data.


