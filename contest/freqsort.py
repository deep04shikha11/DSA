class solution:
    def solve(self,A):
        dct = {}
        A = list(A)
        n = len(A)
        A.sort()
        # ans = []
        for i in range(n):
            if A[i] in dct:
                dct[A[i]] += 1
            else:
                dct[A[i]] = 1
        sortedDict = sorted(dct.items(), key=lambda x:x[1],reverse=True)
        str1 = ''
        for i in (sortedDict):
            for j in range(i[1]):
                str1 += i[0]
        return str1


A = 'pvgcuhrydk'
obj = solution()
print(obj.solve(A))