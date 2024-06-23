from collections import defaultdict, deque

def find_bridges(n, edges):
    # This function finds all the bridges in the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    bridges = []
    time = [0]
    
    def dfs(u):
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if disc[v] == -1:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return bridges

def build_tree(n, edges, bridges):
    # This function builds the resultant tree from the original graph and its bridges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        visited = [-1] * n
        queue = deque([start])
        visited[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
        return visited
    
    components = [-1] * n
    component_id = 0
    
    def assign_component(u):
        queue = deque([u])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if components[neighbor] == -1 and (node, neighbor) not in bridge_set and (neighbor, node) not in bridge_set:
                    components[neighbor] = component_id
                    queue.append(neighbor)
    
    bridge_set = set(bridges)
    for i in range(n):
        if components[i] == -1:
            components[i] = component_id
            assign_component(i)
            component_id += 1
    
    tree = defaultdict(list)
    for u, v in bridges:
        comp_u = components[u]
        comp_v = components[v]
        if comp_u != comp_v:
            tree[comp_u].append(comp_v)
            tree[comp_v].append(comp_u)
    
    return tree

def find_diameter(tree):
    # This function finds the diameter of a tree using BFS twice
    def bfs(start):
        visited = {}
        queue = deque([start])
        visited[start] = 0
        farthest_node = start
        max_distance = 0
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
                    if visited[neighbor] > max_distance:
                        max_distance = visited[neighbor]
                        farthest_node = neighbor
        return farthest_node, max_distance
    
    start_node = next(iter(tree))
    farthest_node, _ = bfs(start_node)
    _, diameter = bfs(farthest_node)
    return diameter

def solve(A, B):
    n = A
    edges = [(u-1, v-1) for u, v in B]
    bridges = find_bridges(n, edges)
    tree = build_tree(n, edges, bridges)
    diameter = find_diameter(tree)
    return diameter

# Example usage:
A = 5
B = [[1, 2], [1, 3], [2, 4], [3, 5]]
print(solve(A, B))  # Output: Diameter of the resultant tree
