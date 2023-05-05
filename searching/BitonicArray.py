class solution:
    def solve(self,A,B):
        n = len(A)
        l = 0
        h = n-1

        # find poc 
        while(l<=h):
            mid = (l+h)//2
            if A[mid]>A[mid+1] and A[mid]>A[mid-1]:
                poc = mid
                break
            elif A[mid]<A[mid+1]:
                l = mid+1
            else:
                h = mid-1

        # before poc 
        l = 0
        r = poc -1
        while(l<=r):
            mid = (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                l = mid+1
            else:
                r = mid-1

        # after poc 
        l = poc 
        r = n-1
        while(l<=r):
            mid = (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                r = mid-1
            else:
                l = mid+1
        return -1


A = [3, 9, 10, 20, 17, 11, 1]
B = 11
obj = solution()
print(obj.solve(A,B))