"""
Copy-pasta for leetcode style tree generation
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


# test code
root = Tests.create_tree_from_flat_list([5, 1, 4, None, None, 3, 6])
assert root.val == 5
assert root.left.val == 1
assert root.right.val == 4
assert root.left.left.val is None
assert root.left.right.val is None
assert root.right.left.val == 3
assert root.right.right.val == 6
