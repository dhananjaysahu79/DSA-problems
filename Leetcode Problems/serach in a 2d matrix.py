# binary search in a matrix
# O(logn + logm)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix) - 1

        while a <= b:
            mid = (a + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                a = mid + 1
            else:
                d = len(matrix[0]) - 1
                c = 0
                while c <= d:
                    mid2 = (c + d) // 2
                    if target == matrix[mid][mid2]: return True
                    elif target > matrix[mid][mid2]:
                        c = mid2 + 1
                    else: d = mid2 - 1
                return False