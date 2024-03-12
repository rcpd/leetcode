"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
"""
from typing import Optional


class Tests:
    @staticmethod
    def create_tree_from_flat_list(value_list):
        """
        convert a list into a binary tree, return the root
        """
        from collections import deque

        # initialize the fringe
        value = iter(value_list)
        root = TreeNode(next(value))
        fringe = deque([root])

        # BFS traversal
        while True:
            # process next node
            head = fringe.popleft()
            try:
                # link & queue children
                head.left = TreeNode(next(value))
                fringe.append(head.left)
                head.right = TreeNode(next(value))
                fringe.append(head.right)
            except StopIteration:
                break

        return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isValidBST(root: Optional[TreeNode]) -> bool:
        valid = Solution.validate(root, float('-inf'), float('inf'))
        print(valid)
        return valid

    @staticmethod
    def validate(root: Optional[TreeNode], floor, ceiling):
        # empty branches serialized as TreeNode(None), children initialized as None
        if not root or root.val is None:
            return True

        # test within valid range
        print(root.val, floor, ceiling, not (root.val <= floor or root.val >= ceiling))
        if root.val <= floor or root.val >= ceiling:
            return False

        # left branch decreases ceiling, right branch increases floor
        return Solution.validate(root.left, floor, root.val) and \
            Solution.validate(root.right, root.val, ceiling)


# test code
e1 = Tests.create_tree_from_flat_list([2, 1, 3])
e2 = Tests.create_tree_from_flat_list([5, 1, 4, None, None, 3, 6])
e3 = Tests.create_tree_from_flat_list([1])
e4 = Tests.create_tree_from_flat_list([5, 4, 6, None, None, 3, 7])

assert Solution.isValidBST(e1)
assert not Solution.isValidBST(e2)
assert Solution.isValidBST(e3)
assert not Solution.isValidBST(e4)
