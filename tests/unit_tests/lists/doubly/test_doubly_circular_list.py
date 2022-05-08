import unittest
from lists.doubly.circular_linked_list import DoublyCircularList
import unittest
from unittest.mock import patch
from io import StringIO


class TestDoublyCircularList(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.doubly_circular_list = DoublyCircularList(3)
    
    def test_append(self):
        self.doubly_circular_list.append(4)
