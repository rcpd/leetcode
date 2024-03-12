"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # recursively walk the nodes
        res = []  # all recursive calls act on shared list
        Solution.helper(root, res)
        return res

    @staticmethod
    def helper(node, res):
        if node:
            # In-order = left, node, right
            Solution.helper(node.left, res)
            res.append(node.val)
            Solution.helper(node.right, res)

    '''
    # iteratively       
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    '''


# test code
n1_3 = TreeNode(val=3, left=None, right=None)
n1_2 = TreeNode(val=2, left=n1_3, right=None)
n1_1 = TreeNode(val=1, left=None, right=n1_2)

n2 = None
n3 = TreeNode(val=1, left=None, right=None)

assert Solution.inorderTraversal(n1_1) == [1, 3, 2]
assert Solution.inorderTraversal(n2) == []
assert Solution.inorderTraversal(n3) == [1]
