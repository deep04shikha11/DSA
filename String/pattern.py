class solution:
    def solve(self,A):
        v=['a','e','i','o','u']
        ans=""
        for i in range(len(A)):
            if A[i]>='a' and A[i]<='z':
                if A[i] in v:
                    ans+='#'
                else:
                    ans+=A[i]
        return ans*2

A="AbcaZeoB"
obj = solution()
print(obj.solve(A))