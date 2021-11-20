

# O(n) time and O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xors = 0
        for i in nums: xors ^= i
        return xors

# O(n // 2) time and O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n-1,2):
            if nums[i] != nums[i+1]: return nums[i]
        return nums[-1]

# O(log n) time and O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0; h = n - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] == nums[mid+1]: mid -= 1
            if (mid - l + 1) & 1: h = mid
            else: l = mid + 1
        return nums[l]