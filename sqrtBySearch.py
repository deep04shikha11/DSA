class SqrtSearch:
    def BinSearch(self,A):
        l = 1
        h = A
        ans = 0
        while(l<=h):
            mid=(l+h)//2
            if mid*mid == A:
                ans = mid
                break
            elif mid*mid >A:
                h = mid-1
            else:
                l= mid+1
                ans = mid
        return ans
obj = SqrtSearch()
print(obj.BinSearch(26))
