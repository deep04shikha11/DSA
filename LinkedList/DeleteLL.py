# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        head = A
        currPos = 0
        currNode = A
        if B == 0:
            head = A.next
            return head
        while currPos < B:
            if currPos == B-1:
                currNode.next = currNode.next.next
            currNode = currNode.next
            currPos += 1
        return head
