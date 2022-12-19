"""
Difficulty - Medium
Lessons learnt with this problem - 
I have to understand tree traversal and not do repetitive coding. 

Logic needs to improve a lot

If you want to store something as a byproduct in a recursive function, a class variable helps a lot !!

I could traverse it properly
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Literal


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MOD: int = 10**9 + 7
        self.ans: Literal[0] = 0
        total_sum = self.traverse_sum_tree(root)
        self.max_sum(root, total_sum)
        return self.ans % MOD

    def traverse_sum_tree(self, root):
        if root is not None:
            return (
                root.val
                + self.traverse_sum_tree(root.left)
                + self.traverse_sum_tree(root.right)
            )
        else:
            return 0

    def max_sum(self, root, total_sum):
        if root is not None:
            sum = (
                root.val
                + self.max_sum(root.left, total_sum)
                + self.max_sum(root.right, total_sum)
            )
            self.ans = max(self.ans, (total_sum - sum) * sum)
            return sum
        else:
            return 0
