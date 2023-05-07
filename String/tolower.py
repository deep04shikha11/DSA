class solution:
    def solve(self,A):
        cnt = 0
        for ch in A:
            if ord(ch)>=65 and ord(ch)<=90:
                A[cnt] = chr(ord(ch)+32)
            cnt += 1
        return A

# converted to lowercase
A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
obj = solution()
print(obj.solve(A))