class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()
        for i in range(9):
            row_set.clear()
            col_set.clear()
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] not in row_set:
                    row_set.add(board[i][j])
                else:
                    return False
                if board[j][i] == '.':
                    pass
                elif board[j][i] not in col_set:
                    col_set.add(board[j][i])
                else:
                    return False
                if i % 3 == 0 and j % 3 == 0:
                    box_set.clear()
                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            if board[k][l] == '.':
                                pass
                            elif board[k][l] not in box_set:
                                box_set.add(board[k][l])
                            else:
                                return False
        return True

            