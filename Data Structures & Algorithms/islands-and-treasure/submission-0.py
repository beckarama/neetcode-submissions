class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        length = 0
        while q:
            length += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != INF:
                        continue
                    
                    grid[nr][nc] = length
                    q.append((nr,nc))                    
