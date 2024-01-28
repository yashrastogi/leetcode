class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = Counter()
        rows = Counter()
        for i in range(len(grid)):
            cur_col = []
            cols[tuple(grid[i])] += 1
        for i in range(len(grid[0])):
            cur_row = []
            for j in range(len(grid)):
                cur_row += [grid[j][i]]
            rows[tuple(cur_row)] += 1
        ret = 0
        for key in rows:
            if key in cols:
                ret += cols[key] * rows[key]
        # print(rows, cols)
        return ret
