# 1975 Maximum matrix sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mini = 9999999
        sm = neg_counter = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] <= 0: neg_counter += 1
                sm += abs(matrix[i][j])
                mini = min(mini,abs(matrix[i][j]))
        return sm - 2 * mini if neg_counter & 1 else sm