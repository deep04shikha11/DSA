import heapq, math
class solution:
    def solve(self,A,B,C):
        max_heap = []
        n = len(A)

        for i in range(n):
            val = A[i]/B[i]
            heapq.heappush(max_heap,(-val, A[i], B[i]))

        sum_of_wght = 0
        tot_val = 0

        while max_heap:
            op = heapq.heappop(max_heap)
            eff_val_rem = C-sum_of_wght
            sum_of_wght += op[2]

            if eff_val_rem >= op[2]:
                tot_val += op[1]
            else:
                residual_val = (-op[0]*eff_val_rem)
                tot_val += residual_val
                break
        
        ans = int(tot_val*1000)
        residual_variance = ans%10
        ans = ans//10

        if residual_variance >9:
            return ans + 1
        else:
            return ans 


A = [60, 100, 120]
B = [10, 20, 30]
C = 50
obj = solution()
print(obj.solve(A,B,C))
