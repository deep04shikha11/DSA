import sys
# Increase the recursion limit
sys.setrecursionlimit(10**6)
from collections import defaultdict, deque

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        n = A
        edges = [(u-1, v-1) for u, v in B]

        # Find bridges
        bridges = self.find_bridges(n, edges)

        # Build tree from bridges
        tree = self.build_tree(n, edges, bridges)

        # Find the diameter of the tree
        if not tree:
            return 0
        return self.tree_diameter(tree)

    def find_bridges(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ids = [-1] * n
        low = [-1] * n
        visited = [False] * n
        bridges = []
        id_counter = 0

        def dfs(at, parent):
            nonlocal id_counter
            visited[at] = True
            ids[at] = low[at] = id_counter
            id_counter += 1

            for to in graph[at]:
                if to == parent:
                    continue
                if not visited[to]:
                    dfs(to, at)
                    low[at] = min(low[at], low[to])
                    if ids[at] < low[to]:
                        bridges.append((at, to))
                else:
                    low[at] = min(low[at], ids[to])

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return bridges

    def build_tree(self, n, edges, bridges):
        tree = defaultdict(list)
        component = [-1] * n
        component_id = 0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Remove bridges from the graph to get the components
        bridge_set = set(bridges)
        def dfs(node):
            stack = [node]
            while stack:
                u = stack.pop()
                if component[u] == -1:
                    component[u] = component_id
                    for v in graph[u]:
                        if component[v] == -1 and (u, v) not in bridge_set and (v, u) not in bridge_set:
                            stack.append(v)

        for i in range(n):
            if component[i] == -1:
                dfs(i)
                component_id += 1

        for u, v in bridges:
            if component[u] != component[v]:
                tree[component[u]].append(component[v])
                tree[component[v]].append(component[u])

        return tree

    def bfs(self, start, graph):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        farthest_node = start
        max_dist = 0

        while queue:
            node, dist = queue.popleft()
            if dist > max_dist:
                max_dist = dist
                farthest_node = node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return farthest_node, max_dist

    def tree_diameter(self, graph):
        if not graph:
            return 0

        start = next(iter(graph.keys()))
        farthest_node, _ = self.bfs(start, graph)
        _, diameter = self.bfs(farthest_node, graph)

        return diameter

# Example usage
A = 6
B = [[1, 2],
    [2, 3],
    [3, 1],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 4]
    ]
obj = Solution()
print(obj.solve(A, B))
