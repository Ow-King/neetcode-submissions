class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                # Check row
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                # Check column
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])

                # Check 3x3 box
                row_index = 3 * (i // 3)
                col_index = 3 * (i % 3)
                curr = board[row_index + j // 3][col_index + j % 3]
                if curr != '.':
                    if curr in box:
                        return False
                    box.add(curr)

        return True
        

        