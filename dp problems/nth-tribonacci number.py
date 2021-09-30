# O(n) space

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        return dp[n]
# O(1) space

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1
        a = 0
        b = c = 1
        for _ in range(3,n+1):
            temp = c
            c += a + b
            a = b
            b = temp
        return c