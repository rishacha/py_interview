from lists.singly.linked_stack import LinkedStack
from io import StringIO
from unittest.mock import patch
import unittest


class TestLinkedStack(unittest.TestCase):
    def setUp(self) -> None:
        # super().setUp()
        self.linked_stack = LinkedStack(5)
        

    def test_stack_created(self):
        self.assertEqual(self.linked_stack.top.data,5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_stack.traverse()
            self.assertEqual(fake_out.getvalue(), "5-->")

    def test_stack_push(self):
        self.linked_stack.push(3)
        self.linked_stack.push(6)
        self.assertEqual(self.linked_stack.size, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_stack.traverse()
            self.assertEqual(fake_out.getvalue(), "5-->3-->6-->")
    
    def test_stack_pop(self):
        self.linked_stack.push(2)
        self.linked_stack.push(7)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_stack.traverse()
            self.assertEqual(fake_out.getvalue(), "5-->2-->7-->")
        self.assertEqual(self.linked_stack.pop(),7)
        self.assertEqual(self.linked_stack.size,2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.linked_stack.traverse()
            self.assertEqual(fake_out.getvalue(), "5-->2-->")
        self.linked_stack.pop()
        self.assertEqual(self.linked_stack.pop(), 5)
        self.assertEqual(self.linked_stack.size, 0)
        with self.assertRaises(Exception) as err:
            self.linked_stack.pop()
        self.assertEqual(str(err.exception),
                         "Cannot pop from empty stack !")

