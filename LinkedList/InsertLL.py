# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):
        head = A
        tail = A
        length = 1
        newNode = ListNode(B)
        while tail.next != None:
            length += 1
            tail = tail.next
        if C >= length:
            tail.next = newNode
            tail = newNode
        elif C <= 0:
            newNode.next = head
            head = newNode
        else:
            currNode = A
            currPos = 0
            while currPos <= C-1:
                if currPos == C-1:
                    newNode.next = currNode.next
                    currNode.next = newNode
                currPos += 1
                currNode = currNode.next
        return head

