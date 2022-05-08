import unittest
from lists.doubly.linked_list import DoublyLinkedList
import unittest
from unittest.mock import patch
from io import StringIO

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.doubly_linked_list = DoublyLinkedList(3)
    def test_append_traverse(self):
        self.doubly_linked_list.append_head(2)
        self.doubly_linked_list.append_tail(5)
        self.assertEqual(self.doubly_linked_list.size,3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_forward()
            self.assertEqual(fake_out.getvalue(), "2<-->3<-->5<-->")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_backward()
            self.assertEqual(fake_out.getvalue(), "5<-->3<-->2<-->")
    
    def test_delete(self):
        self.doubly_linked_list.append_head(2)
        self.doubly_linked_list.append_tail(5)
        self.doubly_linked_list.delete(3)
        self.assertEqual(self.doubly_linked_list.size, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_forward()
            self.assertEqual(fake_out.getvalue(), "2<-->5<-->")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_backward()
            self.assertEqual(fake_out.getvalue(), "5<-->2<-->")
        self.doubly_linked_list.delete(2)
        self.assertEqual(self.doubly_linked_list.size, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_forward()
            self.assertEqual(fake_out.getvalue(), "5<-->")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.doubly_linked_list.traverse_backward()
            self.assertEqual(fake_out.getvalue(), "5<-->")
        self.doubly_linked_list.delete(5)
        self.assertEqual(self.doubly_linked_list.size, 0)
        with self.assertRaises(Exception) as err:
            self.doubly_linked_list.traverse_forward()
        self.assertEqual(str(err.exception), "List is empty !!")
        with self.assertRaises(Exception) as err:
            self.doubly_linked_list.traverse_backward()
        self.assertEqual(str(err.exception), "List is empty !!")

