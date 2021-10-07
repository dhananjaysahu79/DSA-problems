class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        peri = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    peri += 4
                    if i and grid[i-1][j] == 1: peri -= 2
                    if j and grid[i][j-1] == 1: peri -= 2
        return peri
        