# Leetcode: 790 | top level Medium


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        @cache
        def solve(i, prev_gap):
            if i > n: return 0
            if i == n: return not prev_gap
            if prev_gap:
                return (solve(i+2, False) + solve(i+1, True)) % mod
            return (solve(i+1,False) + solve(i+2,False) + 2*solve(i+1,True)) % mod
        return solve(0, False) % mod