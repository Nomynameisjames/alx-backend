#!/usr/bin/env python3
"""
   a class LFUCache that inherits from BaseCaching and is a caching system:
"""

base_caching = __import__('base_caching').BaseCaching

"""
    objectives:
    1- must use self.cache_data - dictionary from the parent class BaseCaching
    2- You can overload def __init__(self): but don’t forget to call the
        parent init: super().__init__()
    3- def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for the
        key key.
        If key or item is None,
            this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
            you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard,
            you must use the LRU algorithm to discard only the least recently
            used
            you must print DISCARD: with the key discarded and following by a
            new line
    4- def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
            return None.
"""


class LFUCache(base_caching):
    """
        LFU caching
    """
    def __init__(self):
        """
            objective 1 and 2
        """
        super().__init__()
        self.cache_data = {}
        self.cache_freq = {}

    def put(self, key, item):
        """
            objective 3
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= base_caching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_freq[key] += 1
                return
            else:
                min_freq = min(self.cache_freq.values())
                for k, v in self.cache_freq.items():
                    if v == min_freq:
                        print(f"DISCARD: {k}")
                        del self.cache_data[k]
                        del self.cache_freq[k]
                        break
        self.cache_data[key] = item
        self.cache_freq[key] = 1

    def get(self, key):
        """
            objective 4
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_freq[key] += 1
        return self.cache_data[key]
