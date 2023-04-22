import sys
sys.setrecursionlimit(10**6)
class Solution:
    def solve(self,A):
        n = len(A)
        self.mergeSort(A,0,n-1)
        print('---final---')
        print(A)

    def mergeSort(self, arr, s, e):
        if s==e:
            return 
        m = (s+e)//2
        self.mergeSort(arr,s,m)
        self.mergeSort(arr,m+1,e)
        self.merge(arr,s,m,e)
        return arr
    
    def merge(self,arr,s,m,e):
        p1 =s
        p2 =m+1
        k = 0
        C = [0]*(e-s+1)
        while p1<=m and p2 <=e:
            if arr[p1]<arr[p2]:
                C[k] = arr[p1]
                k += 1
                p1 += 1
            else:
                C[k] = arr[p2]
                k += 1
                p2 += 1
        while p1<=m:
            C[k] = arr[p1]
            k += 1
            p1 += 1
        while p2 <= e:
            C[k] = arr[p2]
            k += 1
            p2 += 1
             
        # copying the sorted tempArray (merged two sub arrays) to main array C-A
        i = s
        j = 0 
        while i<=e:
            arr[i] = C[j]
            i += 1
            j += 1

A = [1, 4, 10, 2, 1, 5]
obj = Solution()
obj.solve(A)
