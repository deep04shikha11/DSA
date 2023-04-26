class Solution:
# @param A : list of integers
# @return a list of integers
    def solve(self, A):
        from functools import cmp_to_key
        def count_factors(n):
            count = 0
            for i in range(2,int(0.5*n)+1):
                if n%i == 0:
                    count+=1
            return count
        def comparator(a,b):
            #print(a,b)
            factors_a = a[1]
            factors_b = b[1]
            if factors_a < factors_b:
                return -1
            if factors_a == factors_b:
                return a[0]-b[0]
            if factors_a > factors_b:
                return 1
        for i in range(len(A)):
            A[i] = (A[i],count_factors(A[i]))
        # print(A)
        A = sorted(A, key=cmp_to_key(comparator))
        A = [i[0] for i in A]
        return A

A = [4,2,9,2,6,12,7,3,6,8,4,6,7,9,1,1]
fct_srt = Solution()
ans = fct_srt.solve(A)
print(ans)