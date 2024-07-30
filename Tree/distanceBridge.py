import sys

sys.setrecursionlimit(1000000000)
maxm = 200009
maxn = 100009
adj = []
dp = []
level = []
low = []
disc = []
bridges = []
visited = []
comp = []
currComp = 0
edges = []
par = []
bridgeTree = []
ct = 1

def ini():
    global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
    dp = [[-1 for j in range(30)] for i in range(maxn)]
    level = [0] * maxm
    disc = [0] * maxn
    low = [0] * maxn
    bridges = [0] * maxm
    adj = [[] for i in range(maxn)]
    visited = [0] * maxn
    comp = [0] * maxn
    currComp = 0
    edges.clear()
    par = [0] * maxn
    bridgeTree = [[] for i in range(maxn)]
    ct = 1

def bridge(u, p):
    global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
    disc[u] = ct
    low[u] = ct
    ct += 1
    par[u] = p
    visited[u] = 1
    for edge in adj[u]:
        v = edge[0]
        idx = edge[1]
        if visited[v] == 0:
            par[v] = u
            bridge(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges[idx] = 1
        elif par[u] != v:
            low[u] = min(low[u], disc[v])

def dfs1(u):
    global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
    comp[u] = currComp
    for edge in adj[u]:
        if comp[edge[0]] == 0 and bridges[edge[1]] == 0:
            dfs1(edge[0])

def dfs2(u, p):
    global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
    dp[u][0] = p
    level[u] = level[p] + 1
    for v in bridgeTree[u]:
        if v == p:
            continue
        dfs2(v, u)

def lca(u, v):
    global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
    if level[u] < level[v]:
        t = u
        u = v
        v = t
    diff = level[u] - level[v]
    for i in range(0, 25):
        if diff & (1 << i):
            u = dp[u][i]
    if u == v:
        return u
    for i in range(24, -1, -1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]
    return dp[u][0]

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        global maxm, maxn, adj, dp, level, low, disc, bridges, visited, comp, currComp, edges, par, bridgeTree, ct
        ini()
        n = A
        m = len(B)
        for i in range(0, len(B)):
            u = B[i][0]
            v = B[i][1]
            adj[u].append((v, i + 1))
            adj[v].append((u, i + 1))
            edges.append((u, v))
        bridge(1, 0)
        for i in range(1, n + 1):
            if comp[i] == 0:
                currComp += 1
                dfs1(i)
        for i in range(1, m + 1):
            if bridges[i] == 1:
                u = edges[i - 1][0]
                v = edges[i - 1][1]
                bridgeTree[comp[u]].append(comp[v])
                bridgeTree[comp[v]].append(comp[u])
        dfs2(1, 0)
        for j in range(1, 25):
            for i in range(1, n + 1):
                if dp[i][j - 1] != -1:
                    dp[i][j] = dp[dp[i][j - 1]][j - 1]
        ans = []
        for i in range(0, len(C)):
            u = C[i][0]
            v = C[i][1]
            u = comp[u]
            v = comp[v]
            lc = lca(u, v)
            if u == v:
                ans.append(-1)
            else:
                ans.append(level[u] + level[v] - 2 * level[lc])
        return ans

A = 4
B = [[1, 2],[1, 3],[2, 4]]
C = [[1, 2],[1, 4],[3, 4],[4, 4]]
obj = Solution()
print(obj.solve(A,B,C))