"""
Given the root of a binary tree, return its maximum depth.
"""
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = 0
        return Solution.helper(root, depth)

    @staticmethod
    def helper(root: Optional[TreeNode], depth):
        d_left = d_right = 0
        depth += 1
        if root.left:
            d_left = Solution.helper(root.left, depth)
        if root.right:
            d_right = Solution.helper(root.right, depth)
        return max(d_left, d_right, depth)


# test code
e1_l3_0 = TreeNode(val=None)
e1_l3_1 = TreeNode(val=None)
e1_l3_2 = TreeNode(val=15)
e1_l3_3 = TreeNode(val=7)
e1_l2_0 = TreeNode(val=9, left=e1_l3_2, right=e1_l3_3)
e1_l2_1 = TreeNode(val=20, left=e1_l3_0, right=e1_l3_1)
e1_l1_0 = TreeNode(val=3, left=e1_l2_0, right=e1_l2_1)

e2_l2_0 = TreeNode(val=9)
e2_l2_1 = TreeNode(val=20)
e2_l1_0 = TreeNode(val=3, left=e2_l2_0, right=e2_l2_1)

assert Solution.maxDepth(e1_l1_0) == 3
assert Solution.maxDepth(e2_l1_0) == 2

