import java.util.*;

class Solution {
    public int minPathSumIterative(int[][] grid) {
        int[][] dp = grid;
        
        for (int i = 1; i < grid.length; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        for (int j = 1; j < grid[0].length; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        for (int i = 1; i < grid.length; i++) {
            for (int j = 1; j < grid[0].length; j++) {
                dp[i][j] = Math.min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j]);
            }
        }

        return dp[grid.length - 1][grid[0].length - 1];
    }

    public int minPathSumRecursive(int[][] grid) {
        int maxLimit = 40001;
        int[][] memo = new int[grid.length][grid[0].length];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return dfs(0, 0, grid, memo, maxLimit);
    }

    private int dfs(int i, int j, int[][] grid, int[][] memo, int maxLimit) {
        if (i == grid.length - 1 && j == grid[0].length - 1) {
            return grid[i][j];
        } else if (i == grid.length || j == grid[0].length) {
            return maxLimit;
        }
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        memo[i][j] = Math.min(dfs(i, j + 1, grid, memo, maxLimit) + grid[i][j],
                dfs(i + 1, j, grid, memo, maxLimit) + grid[i][j]);
        return memo[i][j];
    }

    public int minPathSum(int[][] grid) {
        return minPathSumIterative(grid);
    }
}
