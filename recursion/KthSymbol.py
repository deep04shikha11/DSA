import sys
sys.setrecursionlimit(10**6)
class Solution:
    def solve(self,A,B):
        sstr = "0"
        for i in range(1,A):
            # print('sstr=',sstr)
            sstr = self.getStr(sstr)
        return int(sstr[B])
    
    def getStr(self,s):
        rstr = ""
        for val in s:
            if val=="0":
                rstr += "1"
            else:
                rstr += "0"
        s += rstr
        return s

        
A = 4
B = 4
obj = Solution()
print(obj.solve(A,B))