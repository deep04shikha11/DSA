# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid):
        negative_count = 0
        for row in grid:
            negative_count += self.binary_search(row)   
        return negative_count 

    def binary_search(self, row):
            low = 0
            high = len(row)-1            
            while low <= high: 
                mid = (low+high)//2             
                if row[mid] < 0:
                    high = mid - 1                    
                else:
                    low = mid + 1                    
            return len(row) - low       

grid = [[5,1,0],[-5,-5,-5]]
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

obj = Solution()
print(obj.countNegatives(grid))

