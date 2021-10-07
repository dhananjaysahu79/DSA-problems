# O(1) space backtracking Approach

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        c = 0

        def find(i,j,c):
            if c == len(word): return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[c]: return False
            board[i][j] = 0
            if find(i,j+1,c+1) or find(i+1,j,c+1) or find(i,j-1,c+1) or find(i-1,j,c+1): return True
            board[i][j] = word[c]


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i,j,c): return True
        return False