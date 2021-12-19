class Solution:
    def decodeString(self, s: str) -> str: 
        
        def isNum(c):
            return c >= '0' and c <= '9'
            
        
        stack = []
        for i in s:
            if i != ']': stack.append(i); continue
            st = m = ''
            while stack[-1] != '[':
                st = str(stack.pop()) + st
                
            stack.pop()

            while len(stack) and isNum(stack[-1]):
                m = stack.pop() + m
            stack.append(int(m) * st)
            
        return ''.join(stack)