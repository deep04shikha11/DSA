class sorting:
    def countSort(self,A):
        F = [0]*(10**5)
        
        for ch in A:
            F[ch] += 1
        
        idx = 0
        for i in range(10**5):
            cnt = F[i]
            if cnt:
                for j in range(cnt):
                    A[idx] = i
                    idx += 1
        return A

A = [9,6,4,11,2,4,1,8]
obj = sorting()
print(obj.countSort(A))