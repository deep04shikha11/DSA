# To find the vertical sum of a binary tree, we can use a hashmap (dictionary in Python) to store the sum of values for each vertical level
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def verticalSum(self, A):
        if not A:
            return []
        sums = {}
        self.vertical_sums(A,0,sums)
        result = []
        min_col = min(sums.keys())
        max_col = max(sums.keys())
        for i in range(min_col, max_col+1):
            result.append(sums[i])
        return result
    
    def vertical_sums(self, root, hd, sums):
        if root is None:
            return
        sums[hd]= sums.get(hd,0)+root.val
        self.vertical_sums(root.left, hd-1,sums)
        self.vertical_sums(root.right, hd+1, sums)
