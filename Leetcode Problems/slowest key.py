class Solution:
    def slowestKey(self, releaseTimes: List[int], keyPressed: str) -> str:
        curr_time = releaseTimes[0]
        curr_key = keyPressed[0]
        for i in range(1,len(keyPressed)):
            if releaseTimes[i] - releaseTimes[i-1] > curr_time:
                curr_time = releaseTimes[i] - releaseTimes[i-1]
                curr_key = keyPressed[i]
            elif releaseTimes[i] - releaseTimes[i-1] == curr_time and keyPressed[i] > curr_key:
                curr_key = keyPressed[i]
        return curr_key
        