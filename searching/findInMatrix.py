class solution:
    def solve(self,A,B):
        n = len(A)
        m = len(A[0])
        ans = -1
        for i in range(n):
            l = 0
            h = m-1
            while(l<=h):
                mid = (l+h)//2            
                if (A[i][mid]==B):
                    ans = 1
                    return ans
                elif(A[i][mid]<B):
                    l = mid+1
                else:
                    h = mid-1
        return ans
        

A = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
B = 0
obj = solution()
print(obj.solve(A,B))