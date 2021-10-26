# O(logN)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 9999999
        l = 0; h = len(nums) - 1

        while l <= h:
            mid = (l+h) // 2

            if nums[l] <= nums[mid]:
                mini = min(mini, nums[l])
                l = mid + 1
            else:
                mini = min(mini, nums[mid])
                h = mid - 1
        return mini