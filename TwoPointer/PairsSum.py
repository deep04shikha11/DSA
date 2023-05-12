class PairOfSum:
    def solve(self,A,B):
        n = len(A)
        p1 = 0
        p2 = n-1
        cnt = 0
        # print('p1=',p1,'p2=',p2,'B=',B)
        while(p1<p2):
            print('p1=',p1,'p2=',p2,'B=',B)
            if (A[p1]+A[p2]==B):
                cnt += 1
                p1 += 1
            if (A[p1]+A[p2])<B:
                p1 += 1
            if (A[p1]+A[p2]>B):
                p2 -= 1
        return cnt

A = [1, 1, 1]
B = 2
obj = PairOfSum()
print(obj.solve(A,B))