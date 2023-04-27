import sys
sys.setrecursionlimit(10**6)
class powerCalculation:
    def solution(self,A,B,C):
        return self.Expo(A,B,C)
    
    def Expo(self, A,B,C):
        if B>1:
            val =(self.Expo(A,B//2,C))
            if B&1==0:
                return (val*val)%C
            else:
                return ((val*val)%C * A%C)%C
        elif B==1:
            return A%C
        else:
            return 1%C
    
A = -1
B = 2
C = 20
obj = powerCalculation()
print(obj.solution(A,B,C))