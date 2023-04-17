#!/usr/bin/env python3
"""
    Simple pagination
    import files
"""
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            method named get_page that takes two integer arguments page with
            default value 1 and page_size with default value 10.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            method named get_hyper that takes the same arguments (and defaults)
            as get_page and returns a dictionary.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data_file = {}
        data_file['page_size'] = len(data)
        data_file['page'] = page
        data_file['data'] = data
        data_file['next_page'] = page + 1 if page < total_pages else None
        data_file['prev_page'] = page - 1 if page > 1 else None
        data_file['total_pages'] = total_pages
        return data_file
