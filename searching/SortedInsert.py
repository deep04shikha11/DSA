class Solution:
    def searchInsert(self,A,B):
        n = len(A)
        l = 0
        h = n-1
        while(l<=h):
            mid = (l+h)//2
            # print("mid=",mid,' B=',B)
            if A[mid]==B:
                return A.index(B)
            elif B<A[0]:
                return 0
            elif B>A[n-1]:
                return n
            elif A[mid]<B:
                l = mid+1
            else:
                h = mid-1
            return l

A = [1, 3, 5, 6]
B = 4 

obj = Solution()
print(obj.searchInsert(A,B))