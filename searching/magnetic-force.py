# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

class solution:
    def checkPlaceCount(self, pos,dst,m):
        n = len(pos)
        last_pos = pos[0]
        ball_plc = 1
        for i in range(1,n):
            if(pos[i]-last_pos >= dst):
                last_pos= pos[i]
                ball_plc += 1
            if ball_plc == m:
                return True
        return False

    def binarySearch_maxDistance(self, pos, m):
        pos.sort()
        n = len(pos)
        l = pos[0]
        h = pos[n-1]-pos[0]
        while(l<h):
            mid =(l+h+1)//2
            check = self.checkPlaceCount(pos,mid,m)
            if check:
                l = mid
            else:
                h = mid-1
        return l

# largest minimum distance
A = [1, 2, 3, 4, 5]
B = 3
obj = solution()
print(obj.binarySearch_maxDistance(A,B))

