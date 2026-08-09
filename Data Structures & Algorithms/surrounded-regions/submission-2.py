class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(x: int, y: int): # Set every node thats touching a node to B
            # Edge found return true
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != 'O': # Break nothing happened 
                return
            board[x][y] = 'B'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'B':
                    board[row][col] = 'O'
                