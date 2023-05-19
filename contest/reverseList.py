
class solution:
    def __init__(self,x):
        self.val = x
        self.next = None
    def solve(self,A):
        current = A
        previous=None
        while(current!=None):
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        A=previous
        return A
        
