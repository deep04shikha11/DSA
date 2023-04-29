class solution:
    def solve(self,A,B,C):
        s = min(B,C)
        e = A*s
        lcm = (B*C)//self.hcf(B,C)
        result = 0
        d= (10**9)+7
        while(s<=e):
            mid = (s+e)//2
            idx = int(mid//B + mid//C - mid//lcm)
            print('idx=',idx, ' A=',A, ' S=',s, ' E=',e, ' mid=',mid, ' lcm=',lcm)
            if(idx>=A):
                result = mid
                e = mid-1
            else:
                s = mid+1
        return int(result % d)

    def hcf(self,A,B):
        if (B==0):
            return A
        return self.hcf(B, A%B)


A = 19
B = 11
C = 13
obj = solution()
print(obj.solve(A,B,C))