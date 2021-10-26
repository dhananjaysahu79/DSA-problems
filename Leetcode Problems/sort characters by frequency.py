class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        for i in s: dic[i] += 1

        arr = []
        for i,j in dic.items():
            arr.append([j,i])
        arr.sort()
        ans = ''
        for i in arr[::-1]:
            ans += i[0]*i[1]
        return ans


        