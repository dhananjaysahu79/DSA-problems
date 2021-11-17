# Problem no: 2073 | Easy
# O(n)

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            time += min(tickets[k], tickets[i])
            if i > k and tickets[i] >= tickets[k]: time -= 1
        return time