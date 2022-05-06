from lists.singly.linked_queue import LinkedQueue
from io import StringIO
from unittest.mock import patch
import unittest


class TestLinkedQueue(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.linked_queue = LinkedQueue(5)
    
    def test_enqueue(self):
        self.linked_queue.enqueue(3)
        self.assertEqual(self.linked_queue.size,2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_queue.traverse()
            self.assertEqual(fake_out.getvalue(), "5-->3-->")

    def test_dequeue(self):
        self.linked_queue.enqueue(3)
        self.linked_queue.enqueue(2)
        self.assertEqual(self.linked_queue.size, 3)
        self.assertEqual(self.linked_queue.dequeue(),5)
        self.assertEqual(self.linked_queue.size, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_queue.traverse()
            self.assertEqual(fake_out.getvalue(), "3-->2-->")

    def test_empty_queue(self):
        empty_queue = LinkedQueue()
        with self.assertRaises(Exception) as err:
            empty_queue.dequeue()
        self.assertEqual(str(err.exception),
                         "List is empty !!")
        



