# how many contiguous character C can get in a given string A when allowed to do at most B num of changes in python3
class Solution:
	def solve(self, A, B, C):
	    maxCount = 0
	    changeCount= 0
	    left = 0
	    for right in range(len(A)):
	        if A[right]!=C:
	            changeCount += 1
            while changeCount>B :
                if A[left]!= C:
                    changeCount -=1
                left += 1
            maxCount = max(maxCount,right-left+1)
        return maxCount

A = 'abacus'
B = 2
C = 'a'

obj = solution()
print(obj.solve(A,B,C))