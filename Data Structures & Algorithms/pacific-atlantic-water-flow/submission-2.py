class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        atlantic, pacific = set(), set()

        def bfs(source, ocean):
            q = deque(source)

            while q:
                r,c = q.popleft()
                ocean.add((r,c))

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) >= 0 and nr != ROWS and nc != COLS and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                        q.append((nr,nc))

        pac = []
        atl = []

        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS - 1))
        
        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS - 1, c))
        
        bfs(pac, pacific)
        bfs(atl, atlantic)
        
        res = []
        for r,c in atlantic:
            if (r,c) in pacific:
                res.append([r,c])
        return res
        
        
        