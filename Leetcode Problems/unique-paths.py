# Recursive dp approach

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        def traverse(i,j,path):
            if i >= m or j >=n: return 0
            if dp[i][j]: return dp[i][j]
            if i == m-1 and j == n-1: return 1

            path1 = traverse(i,j+1,path)
            path2 = traverse(i+1,j,path)
            dp[i][j] = path1+path2
            return path1+path2

        return traverse(0,0,path)