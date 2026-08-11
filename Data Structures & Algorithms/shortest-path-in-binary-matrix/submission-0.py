class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))

        length = 1

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
            
        while q:
            for _ in range(len(q)):
                r, c = q.popleft() 
                
                if (r,c) == (ROWS - 1, COLS - 1):
                    return length
                
                neighbors = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [1, 1], [1, -1], [-1, 1]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    
                    q.append((nr,nc))
                    visit.add((nr,nc))               
            length += 1
        return -1

