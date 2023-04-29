#inversion count using merge sort
import sys
sys.setrecursionlimit(10**6)
class InversionCount:
    def solve(self,A):
        N = len(A)
        mod = 10**9 + 7
        if N == 1:
            return 0 

        def MergeArr(arr,l,mid,end):
            i = l 
            j = mid+1            
            ans = [None] * (end-l+1)
            k = 0
            count = 0
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    ans[k] = arr[i]
                    i += 1
                else:
                    count += mid - i + 1
                    ans[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid:
                ans[k] = arr[i]
                i += 1 
                k += 1
            while j <= end: 
                ans[k] = arr[j]
                j += 1 
                k += 1 
            counter = 0
            for indx in range(l,end+1):
                arr[indx] = ans[counter]
                counter += 1
            return count 


        def invcount(arr,l,r):
            if l == r:
                return 0
            mid = (l+r)// 2
            A = invcount(arr,l,mid)
            B = invcount(arr,mid+1,r) 
            AB = MergeArr(arr,l,mid,r)
            inversioncount = A + B + AB 
            return inversioncount % mod 
        ans = invcount(A,0,N-1) % mod 
        return ans % mod 

A = [28, 18, 44, 49, 41, 14]
in_srt = InversionCount()
ans = in_srt.solve(A)
print(ans)