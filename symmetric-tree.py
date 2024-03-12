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
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        if root:
            if root.left and root.right:
                # initiate the 2 walks
                left_vals = []
                right_vals = []
                Solution.walk_inorder(root.left, left_vals)
                Solution.walk_mirror(root.right, right_vals)

                # debug
                print(left_vals, right_vals)

                # check the results
                if len(left_vals) == len(right_vals):
                    for i in range(0, len(left_vals)):
                        if left_vals[i] != right_vals[i]:
                            return False
                else:
                    return False
            elif root.left or root.right:
                return False
            elif root.left is None and root.right is None:
                return True

        return True

    @staticmethod
    def walk_inorder(node, res):
        # node, left, right
        if node is not None:
            res.append(node.val)
            if node.left:
                Solution.walk_inorder(node.left, res)
            if node.right:
                Solution.walk_inorder(node.right, res)
        else:
            res.append(node)


    @staticmethod
    def walk_mirror(node, res):
        # node, right, left
        if node is not None:
            res.append(node.val)
            if node.right:
                Solution.walk_mirror(node.right, res)
            if node.left:
                Solution.walk_mirror(node.left, res)
        else:
            res.append(node)


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
