class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        lastChange = 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            r, c, time = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nc >= 0 and nr < row and nc < col: # in-bounds
                    if grid[nr][nc] == 1: #fresh fruit
                        grid[nr][nc] = 2 # rot the fruit
                        q.append((nr, nc, time + 1)) # add the neighbors
                        lastChange = time + 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1

        return lastChange

        
                    
        