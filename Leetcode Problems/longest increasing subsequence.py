# First approach is to take an array and we store the maximum subsequence till any index can acieve
# Approach 1: O(n^2)


class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [0] * len(arr)
        for i in range(len(arr)):
            c = 0
            for j in range(i):
                if arr[i] > arr[j]: c = max(c, dp[j])
            dp[i] = c + 1
        return max(dp)

# Approach 2: O(nlogn)
# binary search approach.

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        subs = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i] > subs[-1]: subs.append(arr[i])
            else:
                lower_bound = bisect_left(subs, arr[i], 0, len(subs))
                subs[lower_bound] = arr[i]
        return len(subs)