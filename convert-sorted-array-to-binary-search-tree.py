"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        return Solution.search(nums, 0, len(nums)-1)

    @staticmethod
    def search(nums, left, right):
        # empty list
        if left > right:
            return

        # root is midpoint if sorted
        mid = (left + right) // 2

        # build nodes
        node = TreeNode(val=nums[mid])
        node.left = Solution.search(nums, left, mid-1)  # build everything less than root
        node.right = Solution.search(nums, mid+1, right)  # build everything greater than root

        return node


# test code
Solution.sortedArrayToBST([-10, -3, 0, 5, 9])
Solution.sortedArrayToBST([1, 3])
