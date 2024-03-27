class Solution {
    func minPathSumRecursive(_ grid: [[Int]]) -> Int {
        var memo = [[Int]: Int]()

        func dfs(_ i: Int, _ j: Int) -> Int {
            if i == grid.count - 1 && j == grid[0].count - 1 {
                return grid[i][j]
            } else if i == grid.count || j == grid[0].count {
                return 40001
            }
            if let found = memo[[i, j]] { return found }
            var minSum = 40001
            for (d0, d1) in [(0, 1), (1, 0)] {
                minSum = min(minSum, dfs(i + d0, j + d1) + grid[i][j])
            }
            memo[[i, j]] = minSum
            return memo[[i, j]]!
        }

        return dfs(0, 0)
    }

    func minPathSum(_ grid: [[Int]]) -> Int {
        return minPathSumRecursive(grid)
    }
}