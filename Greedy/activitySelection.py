# Given two integer arrays A and B of size N.
# There are N activities where A[i] denotes the start time of the ith activity and B[i] denotes the finish time of the ith activity.
# Your task is to select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
# Greedy Algo

from operator import itemgetter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def Greedy(self, A, B):
        task = []
        for i in range(len(A)):
            task.append((A[i],B[i]))
            
        task = sorted(task,key=itemgetter(1))
        ans = 1
        curef = task[0] # current reference
        for i in range(1,len(A)):
            if task[i][0]>=curef[1]:
                ans+=1
                curef = task[i]
        return ans

A = [5, 1, 3, 0, 5, 8]
B = [9, 2, 4, 6, 7, 9]
obj = Solution()
print(obj.Greedy(A,B))