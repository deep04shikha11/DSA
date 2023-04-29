class solution:
    def towerOfHanoi(self, A):
        ans = []
        self.toh(A,1,3,2,ans)
        return ans

    def toh(self,n,s,d,h,ans):
            if n == 0: 
                return
            self.toh(n-1,s,h,d,ans)
            ans.append([n,s,d])
            print(n,s,d)
            self.toh(n-1,h,d,s,ans)
            # print('ans=',ans)            
            # return ans

A = 3
obj = solution()
print(obj.towerOfHanoi(A))