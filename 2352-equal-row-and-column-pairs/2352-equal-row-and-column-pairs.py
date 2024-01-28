class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = Counter()
        rows = Counter()
        for i in range(len(grid)):
            cur_col = ''
            for j in range(len(grid[0])):
                cur_col += str(grid[i][j]) + ' '
            cols[cur_col] += 1
        for i in range(len(grid[0])):
            cur_row = ''
            for j in range(len(grid)):
                cur_row += str(grid[j][i]) + ' '
            rows[cur_row] += 1
        ret = 0
        for key in rows:
            if key in cols:
                ret += cols[key] * rows[key]
        return ret