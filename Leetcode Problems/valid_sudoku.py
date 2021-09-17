# Solution 1: One Time traversal (128ms)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_array = [[0] * (n+1) for _ in range(n)]
        col_array = [[0] * (n+1) for _ in range(n)]
        sub_boxes = [[0] * (n+1) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': continue
                curr_num = int(board[i][j])

                if row_array[i][curr_num] or col_array[j][curr_num] or sub_boxes[(i//3)*3 + j//3][curr_num]:
                    return False
                row_array[i][curr_num] += 1
                col_array[j][curr_num] += 1
                sub_boxes[(i//3)*3 + j//3][curr_num] += 1

        return True

# Lets try using sets

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_array = [set() for _ in range(n)]
        col_array = [set() for _ in range(n)]
        sub_boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': continue

                curr_num = int(board[i][j])

                if curr_num in row_array[i] or curr_num in col_array[j] or curr_num in sub_boxes[(i//3)*3 + j//3]:
                    return False

                row_array[i].add(curr_num)
                col_array[j].add(curr_num)
                sub_boxes[(i//3)*3 + j//3].add(curr_num)

        return True

    # Runtime: 96 ms
    # Always use sets and dictionary when counting

