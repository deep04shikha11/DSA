# Sakura and Sasuke
import sys
sys.setrecursionlimit(200000)

class Solution:
    MAX = int(1e5) + 1
    adj = [[] for _ in range(MAX)]
    dep = [0] * MAX
    cnt = [0] * MAX
    par = [[0] * 20 for _ in range(MAX)]

    @staticmethod
    def reset():
        Solution.adj = [[] for _ in range(Solution.MAX)]
        Solution.dep = [0] * Solution.MAX
        Solution.cnt = [0] * Solution.MAX
        Solution.par = [[0] * 20 for _ in range(Solution.MAX)]

    @staticmethod
    def dfs(u, p):
        Solution.dep[u] = Solution.dep[p] + 1
        j = 0
        Solution.par[u][0] = p
        while Solution.par[Solution.par[u][j]][j] > 0:
            Solution.par[u][j + 1] = Solution.par[Solution.par[u][j]][j]
            j += 1

        for v in Solution.adj[u]:
            if v != p:
                Solution.dfs(v, u)

    @staticmethod
    def dfs2(u, p):
        Solution.cnt[u] = 1
        for v in Solution.adj[u]:
            if v != p:
                Solution.dfs2(v, u)
                Solution.cnt[u] += Solution.cnt[v]

    @staticmethod
    def findPar(u, length):
        i = 0
        while length > 0:
            if length & 1:
                u = Solution.par[u][i]
            length >>= 1
            i += 1
        return u

    @staticmethod
    def lca(u, v):
        if Solution.dep[u] < Solution.dep[v]:
            return Solution.lca(v, u)
        u = Solution.findPar(u, Solution.dep[u] - Solution.dep[v])
        if u == v:
            return u

        for i in range(18, -1, -1):
            if Solution.par[u][i] != Solution.par[v][i]:
                u = Solution.par[u][i]
                v = Solution.par[v][i]
        return Solution.par[u][0]

    def solve(self, A, B, C):
        Solution.reset()
        for u, v in B:
            Solution.adj[u].append(v)
            Solution.adj[v].append(u)
        Solution.dfs(1, 0)
        Solution.dfs2(1, 0)

        ans = [0] * len(C)
        for i, (u, v) in enumerate(C):
            if u == v:
                ans[i] = A
                continue

            if Solution.dep[u] < Solution.dep[v]:
                u, v = v, u

            parCommon = Solution.lca(u, v)

            length = Solution.dep[u] + Solution.dep[v] - 2 * Solution.dep[parCommon]
            if length % 2 != 0:
                ans[i] = 0
                continue

            length //= 2
            if Solution.dep[u] > Solution.dep[v]:
                parCommon = Solution.findPar(u, length)
                uu = Solution.findPar(u, length - 1)
                res = Solution.cnt[parCommon] - Solution.cnt[uu]
            else:
                uu = Solution.findPar(u, length - 1)
                vv = Solution.findPar(v, length - 1)
                res = Solution.cnt[1] - Solution.cnt[uu] - Solution.cnt[vv]

            ans[i] = res

        return ans
A = 3
B = [[1, 2],[1, 3]] 
C = [[2, 3],[1, 3],[1, 2]]
obj = Solution()
print(obj.solve(A,B,C))
