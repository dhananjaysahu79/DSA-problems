class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = [0,0]
        for i in position:
            count[i & 1] += 1
        return min(count)