class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        di = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(i, j, vi) -> int:
            grid[i][j] = 0
            ret = 1
            for d in di:
                ix, jx = i+d[0], j+d[1]
                if ix>=0 and jx>=0 and \
                ix<len(grid) and jx<len(grid[0]) and \
                grid[ix][jx] == 1:
                    ret += dfs(ix, jx, vi)
            return ret
                    
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    vi = set()
                    maxArea = max(maxArea, dfs(i, j, vi))
        return maxArea
        