import sys
sys.setrecursionlimit(10**6)

class Solution:
    def solve(self,A):
        N = len(A)
        return self.insertionSort(A, N)
        
    def insertionSort(self, arr, n):
        if n<=1:
            return 
        self.insertionSort(arr, n-1)
        last = arr[n-1]
        j = n-2
        while(j>=0 and arr[j]>last):
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = last
        return arr

A = [4,2,9,2,6,12,7,3,6,8,4,6,7,9,1,1]
in_srt = Solution()
ans = in_srt.solve(A)
print(ans)


