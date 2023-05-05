class solution:
    def solve(self,A,B):
        n = len(A)
        m = len(A[0])
        ans = 0
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
        

A = [[3],[29],[36],[63],[67],[72],[74],[78],[85]]
B = 41
obj = solution()
print(obj.solve(A,B))