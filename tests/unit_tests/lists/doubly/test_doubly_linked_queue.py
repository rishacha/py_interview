import unittest
from lists.doubly.linked_queue import DoublyLinkedQueue
import unittest
from unittest.mock import patch
from io import StringIO


class TestDoublyLinkedQueue(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.doubly_linked_queue = DoublyLinkedQueue(3)
    def test_enqueue(self):
        self.doubly_linked_queue.enqueue(2)
