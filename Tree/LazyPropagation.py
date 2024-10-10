# Too Much Sorting
N = 100001
seg = [[0 for i in range(4*N)] for j in range(10)]
lazy = [[0 for i in range(4*N)] for j in range(10)]
s = ''

def build(node, start, end):
    if start == end:
        for i in range(10):
            seg[i][node] = 0
        seg[int(s[start])][node] = 1
    else:
        mid = (start + end)>>1
        build(node<<1, start, mid)
        build(node<<1|1, mid + 1, end)
        
        for f in range(10):
            seg[f][node] = seg[f][node<<1] + seg[f][node<<1|1]

def update(f, node, start, end, l, r, val):
	if lazy[f][node] != -1:
		seg[f][node] = (end - start + 1)*lazy[f][node]

		if start != end:
			lazy[f][node<<1] = lazy[f][node]
			lazy[f][node<<1|1] = lazy[f][node]
		lazy[f][node] = -1

	if start > end or start > r or end < l:
		return 

	if l <= start and end <= r:
		seg[f][node] = (end - start + 1)*val
		if start != end:
			lazy[f][node<<1] = val
			lazy[f][node<<1|1] = val
		return
	mid = (start + end)>>1
	update(f, node<<1, start, mid, l, r, val)
	update(f, node<<1|1, mid + 1, end, l, r, val)
	seg[f][node] = seg[f][node<<1] + seg[f][node<<1|1]

def query(f, node, start, end, l, r):
	if start > end or start > r or end < l:
		return 0
	if lazy[f][node] != -1:
		seg[f][node] = (end - start + 1)*lazy[f][node]
		if start != end:
			lazy[f][node<<1] = lazy[f][node]
			lazy[f][node<<1|1] = lazy[f][node]
		lazy[f][node] = -1
	if start >= l and end <= r:
		return seg[f][node]
	mid = (start + end) >> 1
	q1 = query(f, node << 1, start, mid, l, r)
	q2 = query(f, node << 1|1, mid + 1, end, l, r)

	return q1 + q2

class Solution:
    def solve(self, A, B, C, D):
        global s, lazy
        s = A
        n = len(s)
        for j in range(10):
        	for i in range(4*n+1):
        	    lazy[j][i] = -1
        build(1, 0, n - 1)
        q = len(B)
        for x in range(q):
            t = B[x]
            l = C[x]
            r = D[x]
            cur = 0
            l -= 1
            r -= 1
            if t == 1:
                for i in range(10):
                    w = query(i, 1, 0, n - 1, l, r)
                    update(i, 1, 0, n - 1, l, r, 0)
                    update(i, 1, 0, n - 1, l + cur, l + cur + w - 1, 1)
                    cur += w
            else:
                for i in range(9, -1, -1):
                    w = query(i, 1, 0, n - 1, l, r)
                    update(i, 1, 0, n - 1, l, r, 0)
                    update(i, 1, 0, n - 1, l + cur, l + cur + w - 1, 1)
                    cur += w
        res = ''
        for i in range(n):
            for j in range(10):
                if query(j, 1, 0, n - 1, i, i):
                    res += str(j)
        return res

# Example usage:
S = "2134"
T = [1, 2]
L = [1, 2]
R = [4, 3]
obj = Solution()
print(obj.solve(S,T,L,R))  # Output: Diameter of the resultant tree