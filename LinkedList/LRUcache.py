class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUcache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.next = self.head

        self.cache = {}
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addAtTail(self,node):
        node.next = self.tail
        node.prev = self.tail.prev
        if(self.tail.prev):
            self.tail.prev.next = node
            self.tail.prev = node
        self.cache[node.key] = node

    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.addAtTail(node)
            return node.val

    def set(self,key,value):
        newNode = Node(key,value)
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.addAtTail(node)
        else:
            if len(self.cache)==self.capacity:
                self.remove(self.head.next)
                self.addAtTail(newNode)
            else:
                self.addAtTail(newNode)

obj = LRUcache(2)
obj.set(0, 10)
obj.set(5, 12)
obj.get(5)
print(obj)

    
