class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic = defaultdict(int)
        for i in words1: dic[i] += 1
        for i in words2:
            if i in dic and dic[i] < 2: dic[i] -= 1
        count = 0
        for i,j in dic.items():
            if j == 0: count += 1
        return count