# Approach 1: O(n^2)


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        for i in range(len(ages)):
            arr.append([scores[i], ages[i]])
        arr.sort()
        dp = [0] * len(ages)
        for i in range(len(ages)):
            sm = 0
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    sm = max(sm, dp[j])
            dp[i] = sm + arr[i][0]
        return max(dp)