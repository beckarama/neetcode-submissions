class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0

        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
        return time if fresh == 0 else -1
        


        