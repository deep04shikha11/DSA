class MyHashSet:
    def __init__(self):
        self.hashset = []
    
    def add(self, key):
        if not self.contains(key):
            self.hashset.append(key)
    
    def remove(self,key):
        if self.contains(key):
            self.hashset.remove(key)
    
    def contains(self,key):
        return True if key in self.hashset else False

obj = MyHashSet()
obj.add(5)
obj.remove(15)
ans = obj.contains(5)

