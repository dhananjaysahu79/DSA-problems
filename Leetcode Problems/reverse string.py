class Solution:
    def reverseString(self, s: List[str]) -> None:

        def reverse(a,b):
            if a > b: return
            s[a], s[b] = s[b], s[a]
            return reverse(a+1, b-1)
        reverse(0, len(s)-1)

        