# Intuition
# It's a brain-teaser,
# all shortest paths have the same cost.

# Prove
# We have 0 <= rowCosts[r], colCosts[c] <= 10^4,
# that means we don't go duplicated path.

# From the view of row index, the best path will be go directly from start x to home x
# From the view of col index, the best path will be go directly from start y to home y

# Explanation
# Firstly move rows, from startPos[0] to homePos[0].
# Secondly move cols, from startPos[1] to homePos[1].
# Sum up the cost for every step.


# Complexity
# Time O(n+m)
# Space O(1)

class Solution:
    def minCost(self, sp: List[int], hp: List[int], rCost: List[int], cCost: List[int]) -> int:
        cost = 0
        cost += sum(cCost[min(hp[1],sp[1]) : max(hp[1],sp[1])+1])
        cost -= cCost[sp[1]] 
        cost += sum(rCost[min(hp[0],sp[0]) : max(hp[0],sp[0])+1])
        cost -= rCost[sp[0]]
        return cost
            
        