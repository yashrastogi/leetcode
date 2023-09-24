class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        test = [[1,1],
                [2,1]]

        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] not in row_set:
                    row_set.add(board[i][j])
                elif board[i][j] != '.':
                    print(board[i][j], row_set, "row")
                    return False
            col_set = set()
            for j in range(9):
                if board[j][i] not in col_set:
                    col_set.add(board[j][i])
                elif board[j][i] != '.':
                    print(board[j][i], col_set, "col")
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_set = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        # print(k, l)
                        if board[k][l] not in box_set:
                            box_set.add(board[k][l])
                        elif board[k][l] != '.':
                            print(board[k][l], box_set, "box")
                            return False
                # print("next_box")
        return True

            