# Dijkstra's algorithm to calculate minimum time for a signal to reach  all other nodes
import heapq
class solution:
    def solve(self,A,B,C):
        nodes = set(range(1,(C+1)))
        edges = A
        starting_node = B
        graph = {}
        for edge in edges:
            u, v, w = edge
            if u not in graph:
                graph[u] = []
            graph[u].append((v,w))
        distances = { node : float('inf') for node in nodes}
        distances[starting_node] = 0
        qu = [(0,starting_node)]
        while qu:
            curr_time, curr_node = heapq.heappop(qu)
            if curr_time > distances[curr_node]:
                continue
            if curr_node in graph:
                for neighbour , edge_time in graph[curr_node]:
                    new_time = curr_time + edge_time
                    if new_time < distances[neighbour]:
                        distances[neighbour] = new_time
                        heapq.heappush(qu,(new_time,neighbour))
        if any(time==float('inf') for time in distances.values()):
            return -1
        return max(distances.values())

A = [[1,2,1],[2,3,2],[1,3,4]]
B = 1
C = 3
obj = solution()
print(obj.solve(A,B,C))
