"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def connect(root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        print(root.val)

        if root.left:
            # inner link: children left to right
            root.left.next = root.right

            # outer link: right child to left child of root sibling
            # (roots are linked from the previous iteration)
            if root.next:
                root.right.next = root.next.left

            # continue recursing
            Solution.connect(root.left)
            Solution.connect(root.right)

        if root.left and root.left.val and root.left.next:
            print('\t', root.left.val, root.left.next.val)
        elif root.left and root.left.val:
            print('\t', root.left.val, None)

        if root.right and root.right.val and root.right.next:
            print('\t', root.right.val, root.right.next.val)
        elif root.right and root.right.val:
            print('\t', root.right.val, None)

        return root


class Tests:
    @staticmethod
    def create_tree_from_flat_list(value_list):
        """
        convert a list into a binary tree, return the root
        """
        from collections import deque

        if not value_list:
            return []

        # initialize the fringe
        value = iter(value_list)
        root = Node(next(value))
        fringe = deque([root])

        # BFS traversal
        while True:
            # process next node
            head = fringe.popleft()
            try:
                # link & queue children
                head.left = Node(next(value))
                fringe.append(head.left)
                head.right = Node(next(value))
                fringe.append(head.right)
            except StopIteration:
                break

        return root


# test code
e1 = Tests.create_tree_from_flat_list([1,2,3,4,5,6,7])  # output = [1,#,2,3,#,4,5,6,7,#]
e2 = Tests.create_tree_from_flat_list([])  # output = []

Solution.connect(e1)
