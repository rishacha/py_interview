from lists.singly.linked_list import LinkedList
from io import StringIO
from unittest.mock import patch
import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.sample_list = LinkedList(1)

    def test_traversal(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "1-->")

    def test_append_tail(self):
        self.sample_list.append(2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "1-->2-->")

    def test_append_head(self):
        self.sample_list.append_head(3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "3-->1-->")

    def test_exception(self):
        with self.assertRaises(Exception):
            sample_list = LinkedList()
        with self.assertRaises(Exception):
            sample_list= LinkedList(None)

    def test_deletion(self):
        ## Setup
        self.sample_list.append(3)
        self.sample_list.delete(4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.sample_list.traverse()
            self.assertEqual(fake_out.getvalue(), "1-->3-->")

    def test_deletion_root(self):
        with self.assertRaises(Exception) as err:
            self.sample_list.delete(1)
        self.assertEqual(
            'Cannot delete single element root !',
            str(err.exception)
        )
