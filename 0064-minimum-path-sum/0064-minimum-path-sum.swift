class Solution {
    func minPathSumIterative(_ grid: [[Int]]) -> Int {
        var dp = grid
        for i in 1..<grid.count { dp[i][0] = dp[i - 1][0] + grid[i][0] }
        for j in 1..<grid[0].count { dp[0][j] = dp[0][j - 1] + grid[0][j] }
        for i in 1..<grid.count {
            for j in 1..<grid[0].count {
                dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j])
            }
        }
        return dp[grid.count - 1][grid[0].count - 1]
    }

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
            memo[i][j] = min(dfs(i, j + 1) + grid[i][j], dfs(i + 1, j) + grid[i][j])
            return memo[i][j]
        }
        return dfs(0, 0)
    }

    func minPathSum(_ grid: [[Int]]) -> Int {
        return minPathSumIterative(grid)
    }
}