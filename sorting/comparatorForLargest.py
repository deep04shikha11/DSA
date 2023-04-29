class solution:
    def largestNum(self,A):
        if len(set(A)) == 1:
            return A[0]
        from functools import cmp_to_key
        def comparator(a,b):
            if a+b > b+a:
                return 1
            if b+a > a+b:
                return -1
            return 0
        A = [str(i) for i in A]
        A = sorted(A, key=cmp_to_key(comparator), reverse=True)
        return "".join(A)

A = [3, 30, 34, 5, 9]
obj = solution()
print(obj.largestNum(A))
            
            
        