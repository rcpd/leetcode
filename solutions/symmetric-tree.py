"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSymmetric(root):
        if root is None:
            return True
        else:
            return Solution.isMirror(root.left, root.right)

    @staticmethod
    def isMirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outerPair = Solution.isMirror(left.left, right.right)
            innerPair = Solution.isMirror(left.right, right.left)
            return outerPair and innerPair
        else:
            return False


# test code
e1_l3_0 = TreeNode(val=3)
e1_l3_1 = TreeNode(val=4)
e1_l3_2 = TreeNode(val=4)
e1_l3_3 = TreeNode(val=3)
e1_l2_0 = TreeNode(val=2, left=e1_l3_0, right=e1_l3_1)
e1_l2_1 = TreeNode(val=2, left=e1_l3_2, right=e1_l3_3)
e1_l1_0 = TreeNode(val=1, left=e1_l2_0, right=e1_l2_1)

e2_l3_0 = TreeNode(val=None)
e2_l3_1 = TreeNode(val=3)
e2_l3_2 = TreeNode(val=None)
e2_l3_3 = TreeNode(val=3)
e2_l2_0 = TreeNode(val=2, left=e2_l3_0, right=e2_l3_1)
e2_l2_1 = TreeNode(val=2, left=e2_l3_2, right=e2_l3_3)
e2_l1_0 = TreeNode(val=1, left=e2_l2_0, right=e2_l2_1)

e3_l3_0 = TreeNode(val=None)
e3_l3_1 = TreeNode(val=3)
e3_l3_2 = TreeNode(val=3)
e3_l3_3 = TreeNode(val=None)
e3_l2_0 = TreeNode(val=2, left=e3_l3_0, right=e3_l3_1)
e3_l2_1 = TreeNode(val=2, left=e3_l3_2, right=e3_l3_3)
e3_l1_0 = TreeNode(val=1, left=e3_l2_0, right=e3_l2_1)

e4_l3_0 = TreeNode(val=3)
e4_l3_1 = TreeNode(val=None)
e4_l3_2 = TreeNode(val=3)
e4_l3_3 = TreeNode(val=None)
e4_l2_0 = TreeNode(val=2, left=e4_l3_0, right=e4_l3_1)
e4_l2_1 = TreeNode(val=2, left=e4_l3_2, right=e4_l3_3)
e4_l1_0 = TreeNode(val=1, left=e4_l2_0, right=e4_l2_1)

assert Solution.isSymmetric(e1_l1_0)
assert not Solution.isSymmetric(e2_l1_0)
assert Solution.isSymmetric(e3_l1_0)
assert not Solution.isSymmetric(e4_l1_0)
