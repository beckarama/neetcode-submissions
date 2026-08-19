class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        visit = set()

        def dfs(r, c):
            if (r, c) in visit:
                return False

            if [r, c] == destination:
                return True

            visit.add((r, c))

            dirX = [0, 1, 0, -1]
            dirY = [-1, 0, 1, 0]

            for i in range(4):
                nr = r
                nc = c

                while (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    maze[nr][nc] == 0
                ):
                    nr += dirX[i]
                    nc += dirY[i]

                nr -= dirX[i]
                nc -= dirY[i]

                if dfs(nr, nc):
                    return True

            return False

        return dfs(start[0], start[1])