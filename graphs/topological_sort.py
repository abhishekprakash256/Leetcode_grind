"""

the code to make the topological sort in the graph 
"""


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # The stack now contains the topological ordering
        return stack[::-1]

# Example usage:
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:", g.topological_sort())
