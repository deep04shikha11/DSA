import sys
sys.setrecursionlimit(10**6)
class magicalNum:
    def solution(self,A):
        finalSum = 0
        while A>0:
            finalSum += self.digitSum(A)
            A = self.digitSum(A)
            if(A==1):
                return 1
            if(A<10):
                return 0


    def digitSum(self,A):
        Asum = 0
        while(A>0):
            rem = A%10
            Asum += rem
            A = A//10
        return Asum

A = 1291
obj = magicalNum()
print(obj.solution(A))