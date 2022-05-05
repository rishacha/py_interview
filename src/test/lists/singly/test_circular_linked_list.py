from lists.singly.circular_linked_list import CircularList
from io import StringIO
from unittest.mock import patch
import unittest

class TestCicularList(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.circular_list = CircularList(4)
    
    def test_append(self):
        self.circular_list.append(5)
        self.assertEqual(self.circular_list.root, self.circular_list.root.next.next)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.circular_list.traverse()
            self.assertEqual(fake_out.getvalue(), "4-->5-->ROOT-CIRCULAR")

    def test_delete(self):
        self.circular_list.append_head(7)
        self.circular_list.append_tail(10)

        self.circular_list.delete(4)
        self.assertEqual(self.circular_list.root,
                         self.circular_list.root.next.next)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.circular_list.traverse()
            self.assertEqual(fake_out.getvalue(), "7-->10-->ROOT-CIRCULAR")
        
        self.circular_list.append(8)
        self.circular_list.delete(10)
        self.assertEqual(self.circular_list.root,
                         self.circular_list.root.next.next)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.circular_list.traverse()
            self.assertEqual(fake_out.getvalue(), "7-->8-->ROOT-CIRCULAR")

    def test_search(self):
        self.circular_list.append_head(7)
        self.circular_list.append_tail(10)
        self.assertEqual(self.circular_list.search(7), True)
        self.assertEqual(self.circular_list.search(4), True)
        self.assertEqual(self.circular_list.search(9), False)
        self.assertEqual(self.circular_list.search(10),True)

    def test_exceptions(self):
        empty_circular_queue = CircularList()
        with self.assertRaises(Exception) as err:
            empty_circular_queue.delete(4)
        self.assertEqual(str(err.exception),
                         "Cannot delete empty list !")
        
        with self.assertRaises(Exception) as err:
            self.circular_list.delete(None)
        self.assertEqual(str(err.exception),
                         "Cannot delete None type data from circular list")
        empty_circular_queue = CircularList()
        with self.assertRaises(Exception) as err:
            empty_circular_queue.search(4)
        self.assertEqual(str(err.exception),
                         "Cannot search empty list !")

        with self.assertRaises(Exception) as err:
            self.circular_list.search(None)
        self.assertEqual(str(err.exception),
                         "Cannot search None type data from circular list")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.circular_list.delete(5)
            self.assertEqual(fake_out.getvalue(),
                             "5 not found in Circular List\n")

