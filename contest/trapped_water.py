# To compute the amount of water that can be trapped after raining using two-pointer approach

class solution:
    def trap(self, height):
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        trapped_water = 0
        for i in range(1, n-1):
            min_side = min(left_max[i-1], right_max[i+1])
            if min_side > height[i]:
                trapped_water += min_side - height[i]

        return trapped_water


A = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = solution()
print(obj.trap(A))