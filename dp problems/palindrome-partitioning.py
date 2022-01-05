class Solution:
    def __init__(self):
        self.dic = {}
        
    def isPalindrome(self, s):
        a = 0; b = len(s) - 1
        while a <= b:
            if s[a] != s[b]: return False
            a += 1; b -= 1
        return True
    
    def partition(self, s):
        if not len(s): return [[]]
        if s in self.dic: return self.dic[s]
        
        n = len(s)
        ans = []
        for i in range(1,n+1):
            if self.isPalindrome(s[:i]):
                for p in self.partition(s[i:]):
                    ans.append([s[:i]] + p)
        self.dic[s] = ans
        return ans