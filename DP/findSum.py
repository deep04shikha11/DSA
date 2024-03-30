# find whether their exist a subset in array A whose sum equal to B
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        dp = [[False]*(B+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1,B+1):
                if A[i-1]<=j:
                    dp[i][j]=dp[i-1][j-A[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[n][B]:
            return 1
        else:
            return 0

A = [3,34,4,12,5,2]
B = 9
obj = Solution()
print(obj.solve(A,B))