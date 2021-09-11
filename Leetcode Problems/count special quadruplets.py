# 1995: Count Special Quadruplets
# A easy and naive solution can be taking the four for loops and calculate the all possibilities
# You will not get TLE for this solution as the question is marked in easy category.
# For python we can directly use combinations O(n^4) if we calculate quadruplets directly
# But we can also optimise the combination by enumerating (But for interview purpose we are not allowed to do that)

# Optimal solution: O(n**2)

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # We will take a dictionary to store the sums of nums[a] and nums[b]
        dic = defaultdict(int)
        n = len(nums)
        quadruplets_count = 0

        # we will take two constants c and b for each iteration of first for loop,
        # b would be one lesser than c
        # then we will loop from left to pickup a for summing up with our constant b
        # Similarly we will loop from right side of c to pickup d to calculate (d-c)
        for c in range(2,n):
            b = c-1
            for a in range(c-1):
                dic[nums[a] + nums[b]] += 1
            for d in range(c+1,n):
                # nums[a] + nums[b] == nums[d] - nums[c]
                quadruplets_count += dic[nums[d] - nums[c]]
        return quadruplets_count