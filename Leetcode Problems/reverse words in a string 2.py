# Naive
def reverseWords(self, s: str) -> str:
        n = len(s)
        prev = 0
        ans = ''
        for i in range(n):
            if i == n - 1 or s[i] == ' ':
                u = n if i == n-1 else i
                ans += s[prev: u][::-1] + ('' if i == n-1 else ' ')
                prev = i + 1
        return ans


# Recursive

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(a,b,arr):
            if a > b:
                return a,b,arr
            arr[a],arr[b] = arr[b], arr[a]
            return reverse(a+1,b-1,arr)


        words = s.split(" ")
        for i in range(len(words)):
            a,b,words[i] = reverse(0,len(words[i])-1,list(words[i]))
            words[i] = ''.join(words[i])
        return ' '.join(words)
        
# One-liner (fastest among all)

class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join([i[::-1] for i in s.split(" ")])