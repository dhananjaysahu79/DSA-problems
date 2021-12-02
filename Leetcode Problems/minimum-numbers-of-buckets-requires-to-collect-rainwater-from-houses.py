# O(n) Solution
# Leetcode: 2086 | Medium

class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        count = prev_bucket = 0
        for i in range(n):
            if street[i] == '.': continue
            if prev_bucket and i - prev_bucket == 1: continue
            elif i+1 < n and street[i+1] == '.':
                prev_bucket = i+1
            elif i-1 >= 0 and street[i-1] == '.':
                prev_bucket = i-1
            else: return -1
            count += 1
        return count