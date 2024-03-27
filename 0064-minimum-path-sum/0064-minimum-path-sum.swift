class Solution {
    func minPathSumRecursive(_ grid: [[Int]]) -> Int {
        let maxLimit = 40001
        var memo = Array(repeating: Array(repeating: -1, count: grid[0].count), count: grid.count)

        func dfs(_ i: Int, _ j: Int) -> Int {
            if i == grid.count - 1 && j == grid[0].count - 1 {
                return grid[i][j]
            } else if i == grid.count || j == grid[0].count {
                return maxLimit
            }
            if memo[i][j] != -1 { return memo[i][j] }
            var minSum = maxLimit
            for (d0, d1) in [(0, 1), (1, 0)] {
                minSum = min(minSum, dfs(i + d0, j + d1) + grid[i][j])
            }
            memo[i][j] = minSum
            return memo[i][j]
        }

        return dfs(0, 0)
    }

    func minPathSum(_ grid: [[Int]]) -> Int {
        return minPathSumRecursive(grid)
    }
}