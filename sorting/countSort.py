class sorting:
    def countSort(self,A):
        F = [0]*(10**5)
        
        for ch in A:
            F[ch-1] += 1
        
        idx = 0
        for i in range(10**5):
            cnt = F[i]
            if cnt:
                for j in range(cnt):
                    A[idx] = i+1
                    idx += 1
        return A

A = [4, 2, 1, 3]
obj = sorting()
print(obj.countSort(A))