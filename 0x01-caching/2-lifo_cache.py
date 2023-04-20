#!/usr/bin/env python3
"""
    class LIFOCache inherits from BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching

"""
    objectives:
    1- You must use self.cache_data - dictionary from the parent class
        BaseCaching
    2- You can overload def __init__(self): but don’t forget to call the
    3- def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None,
            this method should not do anything.
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
            discard the last item put in cache (LIFO algorithm)
            print DISCARD: with the key discarded and following by a new line
    4- def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
            return None.
"""


class LIFOCache(BaseCaching):
    """
        class LIFOCache inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        """
            objective 1 and 2
        """
        super().__init__()

    def put(self, key, item):
        """
            objective 3
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            waste = list(self.cache_data.keys())[-2]
            print(f"DISCARD: {waste}")
            del self.cache_data[list(self.cache_data.keys())[-2]]

    def get(self, key):
        """
            objective 4
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
