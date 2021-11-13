# Approch 1 : Brute force Solution O(n**2)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)-1):
            flag = True
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    flag = False
                    break
            if flag: ans.append(0)
        ans.append(0)
        return ans

#Approach 2: Using stack
# O(n)

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(n):
            if len(stack):
                while len(stack) and temp[i] > temp[stack[-1]]:
                    index = stack.pop()
                    ans[index] = i - index
            stack.append(i)
        return ans