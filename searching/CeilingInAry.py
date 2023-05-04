class solution:
    def solve(self, A, B, C):
        n = len(B)
        l = 0
        h = n-1
        ans = -1
        while(l<=h):
            mid = (l+h)//2
            if B[mid]>=C:
                ans = B[mid]  
                h = mid-1
            else:
                l = mid+1
        return ans

A = 5
B = [2, 5, 6, 9, 18]
C = 7

obj = solution()
print(obj.solve(A, B, C))