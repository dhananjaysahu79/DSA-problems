# Recursive dp approach

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 2)
        def ways(x):
            if x == n: return 1
            if x == n + 1: return 0
            if dp[x+1] == -1: dp[x+1] = ways(x+1)
            if dp[x+2] == -1: dp[x+2] = ways(x+2)
            return dp[x+1] + dp[x+2]
        return ways(0)