class solution:
    def solve(self,A,B):
        n = len(B)
        A = list(A)
        ans = [0]*n
        for i in range(n):
            ans[B[i]] = A[i]
        return ''.join(ans)

A = 'aabgs'
B = [3,1,2,4,0]
obj = solution()
print(obj.solve(A,B))