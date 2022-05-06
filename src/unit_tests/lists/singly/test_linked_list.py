from lists.singly.linked_list import LinkedList
from io import StringIO
from unittest.mock import patch
import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.sample_list = LinkedList(data=1)

    def test_empty_node(self):
        with self.assertRaises(Exception) as err:
            self.sample_list.Node(None)
        self.assertEqual(str(err.exception),
                         "Data type cannot be None")
        
    
    def test_empty_list(self):
        empty_list = LinkedList()
        self.assertEqual(empty_list.size,0)

    def test_traversal(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "1-->")

    def test_append_tail(self):
        self.sample_list.append_tail(2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "1-->2-->")
        with self.assertRaises(Exception) as err:
            self.sample_list.append_tail(None)
        self.assertEqual(str(err.exception),
                         "Data type cannot be None")

    def test_append_head(self):
        self.sample_list.append_head(3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "3-->1-->")

    def test_deletion(self):
        ## Setup
        self.sample_list.append_tail(3)
        self.sample_list.delete(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "3-->")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.delete(4)
            self.assertEqual(fake_out.getvalue(), "4 not found in List\n")

        self.sample_list.append_tail(4)
        self.sample_list.append_tail(5)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.delete(4)
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "3-->5-->")

        with self.assertRaises(Exception) as err:
            empty_list = LinkedList()
            empty_list.delete(3)
        self.assertEqual(str(err.exception),
                         "List is empty !!")
        

    def test_deletion_root(self):
        self.sample_list.delete(1)
        self.assertEqual(self.sample_list.size,0)
        with self.assertRaises(Exception) as err:
            self.sample_list.traverse()
        self.assertEqual(str(err.exception), "List is empty !!")

    def test_delete_empty_list(self):
        
        with self.assertRaises(Exception) as err:
            self.sample_list.delete(1)
            self.sample_list.delete(data=None)
        self.assertEqual(str(err.exception),
                         "Data type cannot be None")

    def test_search(self):
        self.sample_list.append_tail(4)
        self.sample_list.append_tail(5)
        
        self.assertEqual(self.sample_list.search(4), True)
        self.assertEqual(self.sample_list.search(6), False)
        with self.assertRaises(Exception) as err:
            self.sample_list.search(None)
        self.assertEqual(str(err.exception), "Data type cannot be None")

        
       
