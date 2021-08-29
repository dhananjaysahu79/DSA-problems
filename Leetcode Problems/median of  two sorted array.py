link = 'https://leetcode.com/problems/median-of-two-sorted-arrays/'

# Solution 1: O((m+n)//2 approach)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        index1 = index2 = 0
        if total_length & 1:
            index1 = index2 = total_length // 2
        else:
            index1 = total_length // 2 - 1
            index2 = index1 + 1

        a = b = c = 0
        val1 = val2 = 0
        while c <= index2:
            if b >= len(nums2) or (a < len(nums1) and nums1[a] <= nums2[b]):
                if c == index1:
                    val1 = nums1[a]
                if c == index2:
                    val2 = nums1[a]
                a += 1

            else:
                if c == index1:
                    val1 = nums2[b]
                if c == index2:
                    val2 = nums2[b]
                b += 1
            c += 1

        return (val1 + val2) / 2

# Approach 2: O(log(m+n))


