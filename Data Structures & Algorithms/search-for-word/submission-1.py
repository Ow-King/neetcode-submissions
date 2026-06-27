class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i >= rows or i < 0 or j >= cols or j < 0 or visited[i][j] or word[k] != board[i][j]:
                return False

            visited[i][j] = True
            
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)

            visited[i][j] = False

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False