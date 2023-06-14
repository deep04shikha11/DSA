class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

from collection import deque
class TraversalBT:
    def zigzagLevelOrder(self,A):
        last = A
        ans = []
        tmp = []
        Q = deque()
        Q.append(A)
        while Q:
            x = Q.popleft()
            tmp.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
            if last == x:
                ans.append(tmp)
                tmp = []
                if q:
                    last = q[-1]
        for i in range(len(ans)):
            if i&1:
                ans[i] = ans[i][::-1]
        return ans

