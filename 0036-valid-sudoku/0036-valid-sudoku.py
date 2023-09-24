class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] not in row_set:
                    row_set.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                if board[j][i] not in col_set:
                    col_set.add(board[j][i])
                elif board[j][i] != '.':
                    return False
                if i % 3 == 0 and j % 3 == 0:
                    box_set = set()
                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            if board[k][l] not in box_set:
                                box_set.add(board[k][l])
                            elif board[k][l] != '.':
                                return False
        return True

            