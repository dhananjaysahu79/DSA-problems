from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rotten = deque()
        oranges = 0
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]: oranges += 1
                if grid[i][j] == 2:
                    flag = True
                    rotten.append([i,j])

        total = cnt_days = 0
        direction = [[-1,0],[0,1],[1,0],[0,-1]]

        while flag:
            curr_size = len(rotten)
            total += curr_size
            flag = False
            for _ in range(curr_size):
                curr_rotten = rotten.popleft()
                for i in direction:
                    x = curr_rotten[0] + i[0]
                    y = curr_rotten[1] + i[1]

                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                        continue
                    grid[x][y] = 2
                    rotten.append([x,y])
                    flag = True
            if flag: cnt_days += 1

        return cnt_days if total == oranges else -1

            