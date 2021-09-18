class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # checking illegal
        if m * n != r * c or (m == r and n == c):
            return mat

        ans = [[0] * c for _ in range(r)]
        counter1 = counter2 = 0
        for i in range(m):
            for j in range(n):
                ans[counter2][counter1] = mat[i][j]
                counter1 += 1
                if counter1 == c:
                    counter1 = 0
                    counter2 += 1
        return ans