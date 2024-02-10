# find the two missing numbers in the given range [1, N+2] from an array of length N using a mathematical approach

class solution:
    def find_missing_numbers(self, arr):
        n = len(arr) + 2
        total_sum = n * (n + 1) // 2  # Sum of first N+2 natural numbers

        arr_sum = sum(arr)

        pivot = (total_sum - arr_sum) // 2

        total_sum_left = pivot * (pivot + 1) // 2
        arr_sum_left = sum(num for num in arr if num <= pivot)

        missing_sum_left = total_sum_left - arr_sum_left
        missing_num1 = missing_sum_left

        missing_num2 = total_sum - arr_sum - missing_num1

        return missing_num1, missing_num2


A = [3, 7, 1, 2, 8, 4, 5]
obj = solution()
print(obj.find_missing_numbers(A))