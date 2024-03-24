# write a function in python3 that search for a specific character within square brackets in a given string and replaces it with another character
import re
class solution:
    def FindAndReplace(self, A, B, C):
        pattern = re.compile(r'\[([^]]*)\]')
        
        def replace(match):
            content = match.group(1)
            new_content = content.replace(B,C)
            return '['+new_content+']'
        
        result = re.sub(pattern,replace,A)
        return result

A = 'e[exe]c'
B = 'e'
C = 'g'
obj = solution()
print(obj.FindAndReplace(A,B,C))