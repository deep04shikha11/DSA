class solution:
    def solve(self,A):
        A = A.split()
        n = len(A)
        p1 = 0
        p2 = n-1
        while(p1<p2):
            A[p1],A[p2] = A[p2], A[p1]
            p1 += 1
            p2 -= 1
        return ' '.join(A)

A = "the sky is blue"
obj = solution()
print(obj.solve(A))
