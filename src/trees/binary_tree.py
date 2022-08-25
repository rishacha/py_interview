"""
This class codes a binary tree in python
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self):
        """
        Insertion here can occur in any arbitrary order since it's not balanced
        """
        pass

    def insert_balanced(self):
        """
        Insert element in a height-balanced order
        """
        pass

    def height_balance(self):
        pass
