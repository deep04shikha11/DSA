# Reverse A singly linked list
class ListNode:
    def __init__(self,x):
        self.val = x
        self.nxt = None

class Solution:
    # A is head of SLL
    def reverseList(self,A):
        cur = A
        prev = None
        while(cur!=None):
            tmp = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = tmp
        A = prev
        return A

# Input A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
# Output 5 -> 4 -> 3 -> 2 -> 1 -> NULL 

