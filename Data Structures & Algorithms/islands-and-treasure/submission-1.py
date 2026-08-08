class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        row = len(grid)
        col = len(grid[0])

        visited = [[False] * col for _ in range(row)]

        # define the bfs
        def bfs(x: int, y: int, prevVal: int):
            if x < 0 or y < 0 or x >= row or y >= col:
                queue.pop(0)
                return
            if grid[x][y] == -1 or visited[x][y]:
                queue.pop(0)
                return
            
            grid[x][y] = prevVal + 1
            visited[x][y] = True

            queue.append((x-1, y, grid[x][y]))
            queue.append((x+1, y, grid[x][y]))
            queue.append((x, y-1, grid[x][y]))
            queue.append((x, y+1, grid[x][y]))

            queue.pop(0)


        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    queue.append((x, y, -1))

        while queue:
            currentBFS = queue[0]
            bfs(currentBFS[0], currentBFS[1], currentBFS[2])

        