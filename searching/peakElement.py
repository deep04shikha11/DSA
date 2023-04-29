class solution:
    def solve(self,A):
        n = len(A)
        l = 0
        h = n-1
        if(len(A)==1):
            return A[0]
        while l<=h:
            mid = (l+h)//2
            # print('mid=',mid,' l=',l,' h=',h)            
            if mid == 0:
                if A[mid]>=A[mid+1]:
                    return A[mid]
                else:
                    l = mid+1
            if mid == n-1:
                if A[mid]>=A[mid-1]:
                    return A[mid]
                else:
                    h = mid-1
            if mid >0 and mid<n-1:
                if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                    return A[mid]
                if A[mid]>A[mid-1]:
                    l = mid+1
                if A[mid]>A[mid+1]:
                    h = mid-1

A = [1, 1000000000, 1000000000]
obj = solution()
print(obj.solve(A))