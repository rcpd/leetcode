"""
Breadth First Search (BFS) of a graph or tree structure
"""
from collections import deque


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
print(rec, it)
assert rec == it == ["A", "B", "C", "D", "E", "F"]
