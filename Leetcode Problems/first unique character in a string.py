class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for i in s: dic[i] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1: return i
        return -1