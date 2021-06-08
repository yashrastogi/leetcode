import pprint

class Solution:
    def solveNQueens(self, n):
        grid = [['.'] * n for _ in range(n)]
        
        def checkClash(i, j):
            directions = [(0, 1), (1, 0), (1, 1), (-1, -1), \
                          (-1, 0), (0, -1), (-1, 1), (1, -1)]
            for d in directions:
                nxt = lambda x, y: (x + d[0], y + d[1])
                ix, jx = nxt(i, j)
                while ix >= 0 and jx >= 0 and ix < n and jx < n:
                    if grid[ix][jx] == "Q":
                        return True
                    ix, jx = nxt(ix, jx)
            return False

        ans = []

        def backtrack(row):
            nonlocal grid
            if row == len(grid):
                return
            for i in range(len(grid[0])):
                grid[row][i] = 'Q'
                if not checkClash(row, i):
                    if row == len(grid) - 1:
                        temp = []
                        for row_el in grid:
                            temp += [''.join(row_el)]
                        ans.append(temp)
                    backtrack(row + 1)
                grid[row][i] = '.'

        backtrack(0)
        return ans