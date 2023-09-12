# InOrder Traversal using stack
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
Class Solution:
    def inorderTraversal(self,root):
        res = []
        if root is None:
            return res
        stack = []
        curr = root
        while curr is not None or len(stack)>0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


