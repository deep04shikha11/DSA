class Solution:
    def check(self, A, mid, B) :
        pages = 0
        students = 1
        for i in range(len(A)) :
            if pages + A[i] <= mid :
                pages += A[i]
            else :
                pages = A[i]
                students += 1
        if students > B :
            return False
        return True

    def books(self, A, B):
        n = len(A)
        l = max(A)
        r = sum(A)
        if B > n :
            return -1
        ans = -1
        while l <= r :
            mid = (l + r) // 2
            if self.check(A, mid, B) :
                ans = mid
                r = mid - 1
            else :
                l = mid + 1
        return ans

