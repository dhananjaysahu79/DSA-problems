# 1921. Eliminate Maximum Number of Monsters
# 1. A naive approach (O(nlogn)) time and O(n) space

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(dist[i] / speed[i])
        time.sort()
        c = 0
        prev = 0
        for i in range(len(time)):
            if time[i] > prev: c += 1
            else: break
            prev += 1
        return c

# 2. Optimal Approach O(n) time and O(n) space
import math
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_times = [0] * len(dist)
        mini = len(dist)
        for i in range(len(dist)):
            time_to_reach_city = math.ceil(dist[i] / speed[i])
            if time_to_reach_city < len(dist):
                arrival_times[time_to_reach_city] += 1
            mini = min(mini, time_to_reach_city)

        if mini >= len(dist): return len(dist)
        monsters = 0
        for i in range(1,len(arrival_times)):
            monsters += arrival_times[i]
            if monsters > i: return i
        return len(dist)

            