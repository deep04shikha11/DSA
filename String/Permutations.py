class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def isEqual(hm1, hm2):
            for k, v in hm1.items():
                if not v == hm2.get(k, 0):
                    return False
            return True

        hm1 = {}
        hm2 = {}
        M = len(A)
        N = len(B)
        if M > N:
            return 0
        for i in range(M):
            hm1[A[i]] = hm1.get(A[i], 0) + 1
            hm2[B[i]] = hm2.get(B[i], 0) + 1

        c = 0
        for i in range(M, N + 1):
            if isEqual(hm1, hm2):
                c += 1
            if i == N:
                return c
            hm2[B[i]] = hm2.get(B[i], 0) + 1
            hm2[B[i - M]] = hm2[B[i - M]] - 1
            if hm2[B[i - M]] == 0:
                hm2.pop(B[i - M])
        return c

A = "abc"
B = "abcbacabc"
obj = Solution()
print(obj.solve(A,B))