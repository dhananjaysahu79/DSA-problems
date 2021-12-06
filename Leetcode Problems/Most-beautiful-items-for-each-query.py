class Solution:
    def maximumBeauty(self, items: List[List[int]], Q: List[int]) -> List[int]:
        
        items.sort()
        n = len(Q)
        ans, dic = [0] * n, {}
        
        for i in range(n):
            if Q[i] in dic: dic[Q[i]].append(i)
            else: dic[Q[i]] = [i]
            
        Q.sort()
        
        itr = maxi = 0
        for i in Q:
            while itr < len(items) and items[itr][0] <= i:
                maxi = max(maxi, items[itr][1])
                itr += 1
            for j in dic[i]: ans[j] = maxi
                
        return ans