# find the equilibrium index of an array

class Solution:
    def equilibrium_index(arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            total_sum -= arr[i]

            if left_sum == total_sum:
                return i

            left_sum += arr[i]

        return -1

A =  [-7, 1, 5, 2, -4, 3, 0]
obj = Solution()
print(obj.equilibrium_index(A))