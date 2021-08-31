class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxi = c = 0
        for i in range(len(s)):
            if s[i] in dic:
                c = min(c+1,i-dic[s[i]])
            else: c += 1
            maxi = max(maxi,c)
            dic[s[i]] = i
        return maxi