def boardPrettyPrint(board):
    for a in board:
        for b in a:
            print(b, end=' ')
        print()
    print()
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs1(i, j, visited):
            if (i, j) in visited: return
            visited.add((i, j))
            board[i][j] = 'E'
            for p in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ix, jx = i + p[0], j + p[1]
                if ix < 0 or ix > len(board)-1 \
                or jx < 0 or jx > len(board[0])-1:
                    continue
                if board[ix][jx] == 'O':
                    dfs1(ix, jx, visited)
               
            
        def dfs2(i, j, visited):
            if i <= 0 or i >= len(board)-1 \
            or j <= 0 or j >= len(board[0])-1:
                    return
            if (i, j) in visited: return
            visited.add((i, j))
            if board[i][j] == 'O':
                board[i][j] = 'X'
            for p in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ix, jx = i + p[0], j + p[1]
                dfs2(ix, jx, visited)
        
        boardPrettyPrint(board)
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                # dfs for O nodes on border,
                # to mark as seperate and not captured
                if board[i][j] == 'O' and (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1):
                    dfs1(i, j, visited)
        
        boardPrettyPrint(board)
        
        # dfs for middle O not connected to board therefore captured
        visited = set()
        dfs2(1, 1, visited)
        
        boardPrettyPrint(board)
        
        # reset E to O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                    
        boardPrettyPrint(board)