class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        visit = set()
        q = deque([(start[0], start[1])])
        visit.add((start[0], start[1]))

        while q:
            r, c = q.popleft()

            if (r, c) == (destination[0], destination[1]):
                return True

            for dr, dc in directions:
                nr = r
                nc = c

                while (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    maze[nr][nc] == 0
                ):
                    nr += dr
                    nc += dc

                nr -= dr
                nc -= dc

                if (nr, nc) not in visit:
                    visit.add((nr, nc))
                    q.append((nr, nc))

        return False