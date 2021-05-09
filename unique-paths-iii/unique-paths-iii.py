class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        starti, startj = 0, 0
        non_obs = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    starti, startj, = i, j
                if grid[i][j] >= 0:
                    non_obs += 1
        count = 0
        
        def dfs(i, j, remain):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] < 0:
                return
            nonlocal count
            if grid[i][j] == 2 and remain == 1:
                count += 1
                return
            
            temp = grid[i][j]
            grid[i][j] = -4
            
            remain-=1
            
            dfs(i+1, j, remain)
            dfs(i, j+1, remain)
            dfs(i-1, j, remain)
            dfs(i, j-1, remain)
            
            grid[i][j] = temp
            
        
        dfs(starti, startj, non_obs)
        return count