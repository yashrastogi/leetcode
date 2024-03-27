class Solution {
    private int minPathSumRecursive(int[][] grid) {
        int maxLimit = 40001;
        int[][] memo = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            Arrays.fill(memo[i], -1);
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
        int minSum = maxLimit;
        int[][] directions = {{0, 1}, {1, 0}};
        for (int[] direction : directions) {
            int d0 = direction[0], d1 = direction[1];
            minSum = Math.min(minSum, dfs(i + d0, j + d1, grid, memo, maxLimit) + grid[i][j]);
        }
        memo[i][j] = minSum;
        return memo[i][j];
    }

    public int minPathSum(int[][] grid) {
        return minPathSumRecursive(grid);
    }
}
