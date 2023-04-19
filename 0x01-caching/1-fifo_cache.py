#!/usr/bin/env python3
"""
   class FIFOCache that inherits from BaseCaching and is a caching system:
"""
base_caching = __import__('base_caching').BaseCaching

"""
    objectives:
    1- You must use self.cache_data - dictionary from the parent class
      BaseCaching
    2- you can overload def __init__(self): but don’t forget to call the
      parent init: super().__init__()
    3- def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for
        the key key.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                you must discard the first item put in cache (FIFO algorithm)
                you must print DISCARD: with the key discarded and following
                by a new line
    4- def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
            return None.
"""


class FIFOCache(base_caching):
    """
        class FIFOCache that inherits from BaseCaching and is a caching system:
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
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > base_caching.MAX_ITEMS:
            waste = list(self.cache_data.keys())[0]
            print(f"DISCARD: {waste}")
            remove_overflow = self.cache_data[list(self.cache_data.keys())[0]]
            del remove_overflow

    def get(self, key):
        """
            objective 4
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
