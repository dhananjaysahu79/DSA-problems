class Solution:
    def maxArea(self, arr: List[int]) -> int:
        maxi = a = 0
        b = len(arr) - 1
        while a < b:
            maxi = max(maxi, min(arr[a],arr[b]) * (b-a))
            if arr[a] < arr[b]: a += 1
            else: b -= 1
        return maxi