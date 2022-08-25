import unittest
from search.binary_search import binary_search
import unittest
from unittest.mock import patch
from io import StringIO


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.even_list = [1,2,3,4,5,6,7,8]
        self.odd_list = [1,2,3,4,5,6,7,8,9]

    def test_search(self):
        for idx,el in enumerate(self.even_list):
            self.assertEqual(binary_search(self.even_list,len(self.even_list),el),idx)
        for idx,el in enumerate(self.odd_list):
            self.assertEqual(binary_search(self.odd_list,len(self.odd_list),el),idx)