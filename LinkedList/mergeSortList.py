# merge two sorted linked list
class ListNode:
    def __init__(self,val=0,nxt=None):
        self.val = val
        self.next = nxt
class solution:
    def mergeTwoList(self,list1):
        dumy = ListNode()
        curr = dumy
    
        while L1 and L2:
            if l1.val<l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.ext = l2
                l2= l2.next
            curr = curr.next
        
        curr.next = l1 or l2

        return dumy.next

