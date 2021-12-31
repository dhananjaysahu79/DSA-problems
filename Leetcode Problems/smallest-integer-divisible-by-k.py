# Leetcode 1015 | Medium
# Approach 1: Remember when we try to further simplify or try to write a fraction in
# in floating points
# There can be two contidion:
# 1. It will be non recurring ie. 1 / 2 = 0.5 or 1 / 4 = 0.25
# 2. It will be recurring ie. 1 / 3 = 0.3333 or 2 / 7 = 0.2857142875714
# So how we manually divide a fraction? we keep appending 0 at the end in the hope 
# that at some time will be remainder is 0 right?
# But what if remainder will never be 0 then it will be on loop and also the remainder
# always will be in the range [1, denominator - 1]

# In this question, we need to find the n that only contains 1 
# So similarly, we need to detect the loop here, if there is a loop then it cant be possible
# so we return -1
# if we get the zero then we will simply return the length of the number 

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0: return -1
        s = set()
        n = c = 1
        while n % k not in s:
            r = n % k
            if r == 0: return c
            s.add(r)
            n = r * 10 + 1          # We only need the remainder thats why multiplying with r and not n
            c += 1
        return -1

# Time complexity: O(k)
# Space complexity: O(k) for using set

# Approach 2: We can optimised the space of the above code 
# How ? Pigeon hole technique
# We know the remainder can only be in the range 1 to denominator-1, where denominator
# is k here for this problem.
# So we can say that we will only have to run the loop till k iteration if 0 doesn't came
# as remainder then we can say that there is definately a cycle.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0: return -1
        n = 0
        for i in range(k):
            n = (n * 10 + 1) % k     # We only need the remainder like we usually do calculation manually
            if not n: return i+1
        return -1
            