#!/usr/bin/env python3
"""
    Simple pagination
    import files
"""
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            method named get_hyper_index that takes two integer arguments
            index with a None default value and page_size with default
            value 10.
        """
        assert type(index) == int and index > 0
        assert type(page_size) == int and page_size > 0
        data_set = []
        total_pages = math.ceil(len(self.indexed_dataset()) / page_size)
        for i in range(index, index + page_size):
            if i in self.indexed_dataset():
                data_set.append(self.indexed_dataset()[i])
        data_file = {}
        data_file['index'] = index
        data_file['page_size'] = len(data_set)
        data_file['page'] = index // page_size + 1
        data_file['data'] = data_set
        data_file['next_index'] = index + page_size
        data_file['prev_index'] = index - page_size
        data_file['total_pages'] = total_pages
        return data_file
