# Calculate the sum of the first A Sumonacci numbers (modulo 10^9+7).
MOD = 1000000007
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    def solve(self, n, f1, f2):
        s1 = f1
        s2 = f2 + f1
        ss1 = s1
        ss2 = s1 + s2

        if n == 1:
            return ss1
        if n == 2:
            return ss2
        if n < 0:
            return -1

        x = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 0]]
        temp = self.power_matrix(x, n - 2)
        m2 = [[ss2], [s2], [f2], [f1]]
        mn = self.multiply(temp, m2)

        return mn[0][0] % MOD

    def power_matrix(self,A, n):
        if n == 0:
            return self.multiply(A, self.get_identity_mat(len(A)))
        if n == 1:
            return self.multiply(A, self.get_identity_mat(len(A)))

        curr_res = self.power_matrix(A, n // 2)
        x = self.multiply(curr_res, curr_res)
        if n % 2 == 0:
            return x
        return self.multiply(x, A)

    def multiply(self, A, B):
        n = len(A)
        p = len(A[0])
        m = len(B[0])

        if p != len(B):
            return None

        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for k in range(p):
                    tmp = (A[i][k] * B[k][j]) % MOD
                    res[i][j] += (tmp + MOD) % MOD
                    res[i][j] %= MOD
        return res

    def get_identity_mat(self,n):
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1
        return res

A = 2
B = 3
C = 4
obj = Solution()
print(obj.solve(A,B,C))