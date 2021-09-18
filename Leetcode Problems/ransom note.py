class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = len(ransomNote)
        b = len(magazine)
        if a > b: return False

        dic = defaultdict(int)
        for i in ransomNote: dic[i] += 1
        for i in magazine:
            if dic[i]: dic[i] -= 1

        return False if sum(dic.values()) else True

        