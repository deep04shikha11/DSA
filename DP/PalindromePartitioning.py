class solution:
    def minCut(self, A):
        n = len(A)
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        # dp = [-1] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            temp = ""
            minCost = float('inf')
            for j in range(i, n):
                temp += A[j]
                if self.isPalindrome(temp):
                    cost = 0
                    if j + 1 == n:
                        cost = dp[j + 1]
                    else:
                        cost = 1 + dp[j + 1]
                    minCost = min(minCost, cost)
            dp[i] = minCost

        # return self.fn(A, 0, dp)
        return dp[0]
    
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

A = "aab"
obj = solution()
print(obj.minCut(A))
