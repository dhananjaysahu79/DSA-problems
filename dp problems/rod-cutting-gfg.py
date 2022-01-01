class Solution:
    def cutRod(self, price, n):
        
        dp = [0] * (n+1)
        for i in range(n):
            dp[i+1] = price[i]
            for j in range(i,i//2-1,-1):
                dp[i+1] = max(dp[i+1], dp[j] + dp[i+1-j])
        return dp[-1]