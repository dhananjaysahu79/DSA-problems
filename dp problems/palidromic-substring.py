# Leetcode 647
# Approach1: Simply traverse through all subarray and then find check it is palidrome or not
# Time complexity: O(n^2 * m)

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # naive solution or bruteforce
        
        def isPal(s):
            a = 0; b = len(s)-1
            while a <= b:
                if s[a] != s[b]: return False
                a += 1
                b -= 1
            return True
        
        
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPal(s[i:j+1]): count += 1
        return count

# The above solution will give TLE, So we need to optimise the solution further 
# by using the dynamic programming
# Approach 2: O(n**2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n , count = len(s), 0
        dp = [[False] * n for _ in range(n)]
        
        g = 0
        for i in range(n):
            for j in range(n-i):
                if g == 0: dp[j][j+g] = True
                elif g == 1:
                    dp[j][j+g] = s[j] == s[j+1]
                else:
                    dp[j][j+g] = (s[j] == s[j+g] and dp[j+1][j+g-1])
                if dp[j][j+g]: count += 1
            g += 1

        return count
 