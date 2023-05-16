class Solution:
    def threeSumClosest(self,A,B):
        A.sort()
        n = len(A)
        bestDist = float('inf')
        bestSum  = 0
        # print(A)
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                # print('i=',i, 'j=',j, ' k=',k)
                currSum = A[i]+A[j]+A[k]
                currDist = abs(B-currSum)
                # print('currSum=',currSum, ' currDist=',currDist)
                if currDist < bestDist:
                    bestDist = currDist
                    bestSum = currSum
                if currSum < B:
                    j += 1
                else:
                    k -= 1
        return bestSum

A = [-1, 2, 1, -4]
B = 1
obj = Solution()
print(obj.threeSumClosest(A,B))