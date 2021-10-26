# Naive

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp // 10
        if carry:
            ans = [carry]
            for i in digits: ans.append(i)
            return ans
        return digits
# Better

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(i) for i in digits])) + 1
        return list(map(int, str(num)))