class rangeSearch:
    def BinSearch(self,A,B):
        n = len(A)
        l = 0
        h = n-1
        # ans = []
        while(l<=h):
            mid = (l+h)//2
            if A[mid]==B:
                if(mid>0):
                    if(A[mid-1]==B):
                        frst = mid -1
                else:
                    frst = mid
                l = mid+1
            elif A[mid]>B:
                h = mid-1
            else:
                l = mid+1
        for i in range(frst,n):
            if A[i]==B:
                last = i

        if len(A)!=1 and frst ==0 and last ==0:
            return [-1,-1]
        else:
            return [frst,last]
A = [5, 7, 7, 8, 8, 10]
B = 5
obj = rangeSearch()
print(obj.BinSearch(A,B)) 