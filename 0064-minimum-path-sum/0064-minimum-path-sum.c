int min(int a, int b) {
    return a < b ? a : b;
}

int minPathSumIterative(int** grid, int gridSize, int* gridColSize) {
    int dp[gridSize][*gridColSize];
    dp[0][0] = grid[0][0];
    
    for (int i = 1; i < gridSize; i++) {
        dp[i][0] = dp[i - 1][0] + grid[i][0];
    }
    
    for (int j = 1; j < *gridColSize; j++) {
        dp[0][j] = dp[0][j - 1] + grid[0][j];
    }
    
    for (int i = 1; i < gridSize; i++) {
        for (int j = 1; j < *gridColSize; j++) {
            dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j]);
        }
    }
    
    return dp[gridSize - 1][*gridColSize - 1];
}

int minPathSumRecursive(int** grid, int gridSize, int* gridColSize) {
    int maxLimit = 40001;
    int memo[gridSize][*gridColSize];
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            memo[i][j] = -1;
        }
    }

    int dfs(int i, int j) {
        if (i == gridSize - 1 && j == *gridColSize - 1) {
            return grid[i][j];
        } else if (i == gridSize || j == *gridColSize) {
            return maxLimit;
        }
        if (memo[i][j] != -1) { return memo[i][j]; }
        memo[i][j] = min(dfs(i, j + 1) + grid[i][j], dfs(i + 1, j) + grid[i][j]);
        return memo[i][j];
    }

    return dfs(0, 0);
}

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    return minPathSumIterative(grid, gridSize, gridColSize);
}
