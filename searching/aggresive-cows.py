class aggresiveCows:
    def checkPlaceCount(self,cows,dst,total_cow):
        n = len(cows)
        last_pos = cows[0]
        cow_placed = 1
        for i in range(1,n):
            if cows[i]-last_pos >= dst:
                cow_placed += 1
                last_pos = cows[i]
            if cow_placed == total_cow:
                return True
        return False
    
    def max_dist(self,cows, total):
        cows.sort()
        n = len(cows)
        l = 0
        h = cows[n-1]-cows[0]
        while(l<h):
            mid = (l+h+1)//2
            check = self.checkPlaceCount(cows,mid,total)
            if check:
                l= mid
            else:
                h = mid-1
        return l            

# largest minimum distance
A = [1, 2, 3, 4, 5]
B = 3
obj = aggresiveCows()
print(obj.max_dist(A,B))
