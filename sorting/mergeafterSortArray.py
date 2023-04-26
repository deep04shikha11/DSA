class Solution:
    def solve(self,A,B):
        print(self.mergeSort(A, B))
    
    def mergeSort(self,A,B):
        lenA = len(A)
        lenB = len(B)
        C = [0]*(lenA+lenB)
        p1 = 0
        p2 = 0
        k = 0
        while p1<lenA and p2<lenB:
            if A[p1]<B[p2]:
                C[k]= A[p1]
                p1 += 1
                k += 1
            else:
                C[k]= B[p2]
                p2 += 1
                k += 1
        while p1<lenA:
            C[k]= A[p1]
            p1 += 1
            k += 1
        while p2<lenB:
            C[k]= B[p2]
            p2 += 1
            k += 1
        return C 

A = [4, 7, 9 ]
B = [2, 11, 19 ]
sol = Solution()
sol.solve(A,B)




