class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = []
        A.sort()
        print(A)
        ans.append(A[0])
        for i in range(1,n):
            ans.append(ans[i-1]*A[i])
        return ans 

A= [-7,-9,-7,2,-9,7,-8,6,-1]
obj = Solution()
print(obj.solve(A))
