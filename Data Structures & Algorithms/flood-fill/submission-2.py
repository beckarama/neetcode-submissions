class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color == color:
            return image

        def dfs(graph, r, c):
            ROWS, COLS = len(graph), len(graph[0])

            if min(r,c) < 0 or r == ROWS or c == COLS or graph[r][c] != starting_color:
                return
            
            graph[r][c] = color

            dfs(graph, r, c + 1)
            dfs(graph, r, c - 1)
            dfs(graph, r + 1, c)
            dfs(graph, r - 1, c)

        dfs(image, sr, sc)
        return image