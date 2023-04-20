#!/usr/bin/env python3
"""
    a class MRUCache that inherits from BaseCaching and is a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching

"""
    objectives:
    1- must use self.cache_data - dictionary from the parent class BaseCaching
    2- can overload def __init__(self): but don’t forget to call the parent
        init: super().__init__()
    3- def put(self, key, item):
         Must assign to the dictionary self.cache_data the item value for the
         key key.
         If key or item is None,
            this method should not do anything.
         If the number of items in self.cache_data is higher than
         BaseCaching.MAX_ITEMS:
            you must discard the most recently used item (MRU algorithm)
            you must print DISCARD: with the key discarded and following
            by a new line
    4- def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
            return None.
"""


class MRUCache(BaseCaching):
    """
        class MRUCache inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
            objective 1 and 2
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
            objective 3
        """
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache_data[key] = item
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            waste = self.keys.pop(-2)
            print(f"DISCARD: {waste}")
            del self.cache_data[waste]
            self.keys.append(key)

    def get(self, key):
        """
            objective 4
        """
        if key is None or key not in self.keys:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
