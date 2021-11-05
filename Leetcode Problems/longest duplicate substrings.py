# A naive way is to find all the substrings and then identify the duplicate substring of maximum length.
# O(n*n) solution.
# this is a leetcode hard level question and this solution will give TLE.
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        se = set()
        ans = ''
        for i in range(len(s)):
            temp = ''
            for j in range(i,len(s)):
                temp += s[j]
                if temp in se and len(temp) > len(ans): ans = temp
                else: se.add(temp)
        return ans


# Approach 2:

