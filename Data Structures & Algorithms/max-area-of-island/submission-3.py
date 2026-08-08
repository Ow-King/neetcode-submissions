class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # variable for the large island
        rows = len(grid)
        cols = len(grid[0])
        output = 0

        # island visited status
        visited = [[False] * cols for _ in range(rows)]

        # running a dfs
        def dfs(x: int, y: int): 
        # check if it is off the map
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0

            # check if it is visited
            if visited[x][y] or grid[x][y] == 0:
                return 0

            visited[x][y] = True

            # Current square + all connected land
            return (
                1
                + dfs(x - 1, y)
                + dfs(x + 1, y)
                + dfs(x, y - 1)
                + dfs(x, y + 1)
            )

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and not visited[x][y]:
                    output = max(output, dfs(x, y))

        return output

                
                
                
                
