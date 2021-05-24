class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        elif grid[-1][-1] == 1:
            return -1
        if len(grid) == len(grid[0]) and len(grid) == 1:
            return 1
        directions = [[0,1],[1,0],[-1,0],[0,-1], [1,1], [-1,-1], [1,-1], [-1, 1]]
        grid[0][0] = 1
        queue = [(0,0,1)]
        while queue:
            i, j, depth = queue.pop(0)
            if (i,j) == (len(grid)-1, len(grid[0])-1):
                return depth
            for d in directions:
                ix, jx, depthx = i+d[0], j+d[1], depth+1
                if ix>=0 and jx>=0 and ix<len(grid) and jx<len(grid[0]):
                    if grid[ix][jx] == 0:
                        grid[ix][jx] = depthx
                        queue.append((ix,jx,depthx))
                        
        return -1