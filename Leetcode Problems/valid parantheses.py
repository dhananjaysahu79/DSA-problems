link = 'https://leetcode.com/problems/valid-parentheses/'

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','[':']','{':'}'}
        for i in s:
            try:
                if dic[stack[-1]] == i: stack.pop()
                else: stack.append(i)
            except: stack.append(i)
        return False if len(stack) else True
