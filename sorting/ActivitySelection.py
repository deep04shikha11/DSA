A = [5, 1, 3, 0, 5, 8]
B = [9, 2, 4, 6, 7, 9]

class GreedyApproach:
    def solve(self, A, B):
        A = sorted(zip(A,B), key= lambda a:a[1])
        start_time = [i[0] for i in A]
        end_time = [i[1] for i in A]
        cnt = 0
        prv_end_time = 0
        for i in range(len(start_time)):
            if prv_end_time <= start_time[i]:
                cnt += 1
                prv_end_time = end_time[i]
        print(cnt)  

sol = GreedyApproach()
sol.solve(A,B)
