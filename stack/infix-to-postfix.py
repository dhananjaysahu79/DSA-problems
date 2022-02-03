class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        stack = []
        ans = ''
        pre = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        
        for e in exp:
            if e in '+*^-/':
                while len(stack) and pre.get(stack[-1],0) >= pre[e]:
                    ans += stack.pop()
                stack.append(e)
                    
            elif e == ')':
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
                
            elif e == '(':
                stack.append(e)
            
            else: ans += e
        ans += ''.join(stack)
            
        return ans