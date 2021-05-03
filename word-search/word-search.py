def rec(i, j, idx, board, word):
    if idx == len(word):
            return True
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] != word[idx]:
        return False
    temp = board[i][j]
    board[i][j] = ' '
    ret = False
    ret |= rec(i, j-1, idx+1, board, word)
    ret |= rec(i+1, j, idx+1, board, word)
    ret |= rec(i, j+1, idx+1, board, word)
    ret |= rec(i-1, j, idx+1, board, word) 
    board[i][j] = temp
    return ret
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for idx in product(range(len(board)), range(len(board[0]))):
            if board[idx[0]][idx[1]] == word[0] and rec(*idx, 0, board, word):
                return True
        return False
            