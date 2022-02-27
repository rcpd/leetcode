"""
Depth First Search (DFS) of a graph or tree structure
"""


class Graph:
    @staticmethod
    def dfs_recursive(visited, graph, vertex):
        """
        O(V+E) time, (V) space
        replace visited list with set if returned order doesn't matter: O(1) access
        """
        if vertex not in visited:
            visited.append(vertex)
            for node in graph[vertex]:
                Graph.dfs_recursive(visited, graph, node)

        return visited

    @staticmethod
    def dfs_iterative(graph, root):
        """
        O(V+E) time, (V) space
        replace visited list with set if returned order doesn't matter: O(1) access
        """
        stack, visited = [root], []

        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.append(vertex)
            for node in graph[vertex]:
                stack.append(node)

        return visited


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Tree:
    """
    all linear traversals are O(n) time (worst case: skewed tree)
    recursive functions are O(n) time/space (depth / stack frames)
    iterative functions are O(n) time, O(1) space (faster in reality due to function overhead)
    """

    @staticmethod
    def in_order_recursive(root, res):
        """
        left, node, right (left to right)
        on a BST, gives nodes in non-decreasing (ascending) order
        """
        if root:
            Tree.in_order_recursive(root.left, res)
            res.append(root.val)
            Tree.in_order_recursive(root.right, res)
        return res

    @staticmethod
    def reverse_order_recursive(root, res):
        """
        right, node, left (right to left)
        on a BST, gives nodes in non-increasing (descending) order
        """
        if root:
            Tree.reverse_order_recursive(root.right, res)
            res.append(root.val)
            Tree.reverse_order_recursive(root.left, res)
        return res

    @staticmethod
    def pre_order_recursive(root, res):
        """
        node, left, right (top down, left to right)
        useful for copying a tree
        """
        if root:
            res.append(root.val)
            Tree.pre_order_recursive(root.left, res)
            Tree.pre_order_recursive(root.right, res)
        return res

    @staticmethod
    def post_order_recursive(root, res):
        """
        left, right, node (bottom up, left to left)
        useful for deleting a tree
        """
        if root:
            Tree.post_order_recursive(root.left, res)
            Tree.post_order_recursive(root.right, res)
            res.append(root.val)
        return res

    @staticmethod
    def in_order_iterative(root):
        """
        left, node, right (left to right)
        on a BST, gives nodes in non-decreasing (ascending) order
        """
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

    @staticmethod
    def reverse_order_iterative(root):
        """
        right, node, left (right to left)
        on a BST, gives nodes in non-increasing (descending) order
        """
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.left
        return res

    @staticmethod
    def pre_order_iterative(root):
        """
        node, left, right (top down)
        useful for copying a tree
        """
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res

    @staticmethod
    def post_order_iterative(root):
        """
        left, right, node (bottom up, left to left)
        useful for deleting a tree
        """
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return res[::-1]


# driver code

print("dfs traversal of a directed graph (recursive/iterative)")
print("  5")
print(" 3 7")
print("2 4 8\n")
graph = {  # adjacency list (key:val is ordered pair of V,E)
  5: [3, 7],
  3: [2, 4],
  7: [8],
  2: [],
  4: [8],
  8: []
}

rec = Graph.dfs_recursive([], graph, 5)
it = Graph.dfs_iterative(graph, 5)
print(rec)
print(it, "(expected to be different)")
assert rec == [5, 3, 2, 4, 8, 7]
assert it == [5, 7, 8, 3, 4, 2]

# ------------------------------------------------------------------------------------------------------------------

print("\ndfs traversal of a tree (connected acylic undirected graph)")
print("  1")
print(" 2 3")
print("4 5\n")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("in-order: recursive/iterative\n")
rec = Tree.in_order_recursive(root, [])
it = Tree.in_order_iterative(root)
print(rec)
print(it)
assert rec == it == [4, 2, 5, 1, 3]

print("\npre-order recursive/iterative\n")
rec = Tree.pre_order_recursive(root, [])
it = Tree.pre_order_iterative(root)
print(rec)
print(it)
assert rec == it == [1, 2, 4, 5, 3]

print("\npost-order recursive/iterative\n")
rec = Tree.post_order_recursive(root, [])
it = Tree.post_order_iterative(root)
print(rec)
print(it)
assert rec == it == [4, 5, 2, 3, 1]

# ------------------------------------------------------------------------------------------------------------------

print("\ndfs traversal of a binary search tree")
print(" 2")
print("1 3\n")

bst = Node(2)
bst.left = Node(1)
bst.right = Node(3)

print("in order (ascending): recursive/iterative\n")
rec = Tree.in_order_recursive(bst, [])
it = Tree.in_order_iterative(bst)
print(rec)
print(it)
assert rec == it == [1, 2, 3]

print("\nreverse order (descending): recursive/iterative\n")
rec = Tree.reverse_order_recursive(bst, [])
it = Tree.reverse_order_iterative(bst)
print(rec)
print(it)
assert rec == it == [3, 2, 1]
