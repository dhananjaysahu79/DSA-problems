# Problem no: 2075
# Time complexity: O(n) where n is the length of the string

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        col = n // rows

        ans = ''
        for i in range(col):
            for j in range(i,n,col+1):
                ans += encodedText[j]
        return ans.rstrip()