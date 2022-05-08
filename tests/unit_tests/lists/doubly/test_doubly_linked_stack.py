import unittest
from lists.doubly.linked_stack import DoublyLinkedStack
import unittest
from unittest.mock import patch
from io import StringIO


class TestDoublyLinkedStack(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.doubly_linked_stack = DoublyLinkedStack(3)
    
    def test_push(self):
        self.doubly_linked_stack.push(2)
