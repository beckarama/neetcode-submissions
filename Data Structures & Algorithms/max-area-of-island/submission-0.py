class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            count = 1

            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)

            return count
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        return res
                    
        