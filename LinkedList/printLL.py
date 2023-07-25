# Definition for singly-linked list.

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class printList:
    def solve(self,A):
        curr = A
        while curr != None:
            print(curr.val, end='')
            curr = curr.next
        print('')


