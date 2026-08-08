class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        INF = 2147483647

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        # Put all gates into the queue
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))

        # BFS from all gates simultaneously
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < R and
                    0 <= nc < C and
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

        