"""
Breadth First Search (BFS) of a graph or tree structure
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Graph:
    @staticmethod
    def bfs_recursive(graph, queue, visited):
        """
        O(V+E) time, (V) space
        replace visited list with set if returned order doesn't matter: O(1) access
        """
        if not queue:
            return

        vertex = queue.popleft()  # pop(0)
        if vertex not in visited:
            visited.append(vertex)  # root

        for node in graph[vertex]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    
        Graph.bfs_recursive(graph, queue, visited)

        return visited

    @staticmethod
    def bfs_iterative(graph, node):
        """
        O(V+E) time, (V) space
        replace visited list with set if returned order doesn't matter: O(1) access
        """
        visited = [node]
        queue = deque([node])

        while queue:
            vertex = queue.popleft()  # pop(0)
            for node in graph[vertex]:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)

        return visited


class Tree:
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

    @staticmethod
    def bfs_zigag(root):
        if not root:
            return []
        queue = deque([root])
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if even_level:
                res.append(level[::-1])
            else:
                res.append(level)
            even_level = not even_level
        return res


# test code

graph = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "C": ["F"],
  "D": [],
  "E": ["F"],
  "F": []
}

print("  A")
print(" B C")
print("D E F\n")

rec = Graph.bfs_recursive(graph, deque(["A"]), [])
it = Graph.bfs_iterative(graph, "A")
print(rec, it, "\n")
assert rec == it == ["A", "B", "C", "D", "E", "F"]

tree = [3, 9, 20, None, None, 15, 7]
root = Tree.create_tree_from_flat_list(tree)
zigzag = Tree.bfs_zigag(root)
print(tree)
print(zigzag)
assert zigzag == [[3], [20, 9], [None, None, 15, 7]]
