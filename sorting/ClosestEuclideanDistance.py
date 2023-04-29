import math
class CloseToOrigin:
    def solve(self, A, B):
        A = sorted(A, key = lambda a : math.pow((math.pow(a[0],2)+math.pow(a[1],2)), 0.5))
        print('---------')
        print(A)
        return A[:B]

A = [[1, 3],[-2, 2]]
B = 1

obj = CloseToOrigin()
print(obj.solve(A,B))