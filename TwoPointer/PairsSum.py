# two pointer technique to find pairs of integers in a list whose sum is equal to a given value
class PairOfSum:
    def solve(self,A,B):
        n = len(A)
        p1 = 0
        p2 = n - 1
        mod = pow(10, 9) + 7
        ans = 0
        while p1 < p2:
            summ = A[p1] + A[p2]
            if summ < B:
                p1 += 1
            elif summ > B:
                p2 -= 1
            else:
                if A[p1] == A[p2]:
                    x = p2 - p1 + 1
                    ans += ((x * (x - 1)) // 2) % mod  # xC2
                    break
                else:
                    dup1 = 1
                    p1 += 1
                    while A[p1] == A[p1 - 1]:
                        p1 += 1
                        dup1 += 1

                    dup2 = 1
                    p2 -= 1
                    while A[p2] == A[p2 + 1]:
                        p2 -= 1
                        dup2 += 1

                    ans += (dup1 * dup2) % mod

        return ans % mod

A = [1, 1, 1]
B = 2
obj = PairOfSum()
print(obj.solve(A,B))