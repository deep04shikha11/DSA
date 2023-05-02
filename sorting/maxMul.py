class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = []
        A.sort()
        v1 = A[0]*A[1]*A[n-1]
        v2 = A[n-3]*A[n-2]*A[n-1]
        print('v1=',v1,' v2=',v2)
        if v1>v2:
            ans.append([0,1,n-1])
        else:
            ans.append([n-3,n-2,n-1])
        
        return ans 

A= [-7,-9,-7,2,-9,7,-8,6,-1]
obj = Solution()
print(obj.solve(A))
