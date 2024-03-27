#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPathSumIterative(vector<vector<int>>& grid) {
        int dp[grid.size()][grid[0].size()];
        dp[0][0] = grid[0][0];
        
        for (int i = 1; i < grid.size(); i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        
        for (int j = 1; j < grid[0].size(); j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }
        
        for (int i = 1; i < grid.size(); i++) {
            for (int j = 1; j < grid[0].size(); j++) {
                dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j]);
            }
        }
        
        return dp[grid.size() - 1][grid[0].size() - 1];
    }

    int minPathSumRecursive(vector<vector<int>>& grid) {
        int maxLimit = 40001;
        vector<vector<int>> memo(grid.size(), vector<int>(grid[0].size(), -1));

        function<int(int, int)> dfs = [&](int i, int j) {
            if (i == grid.size() - 1 && j == grid[0].size() - 1) {
                return grid[i][j];
            } else if (i == grid.size() || j == grid[0].size()) {
                return maxLimit;
            }
            if (memo[i][j] != -1) { return memo[i][j]; }
            memo[i][j] = min(dfs(i, j + 1) + grid[i][j], dfs(i + 1, j) + grid[i][j]);
            return memo[i][j];
        };

        return dfs(0, 0);
    }

    int minPathSum(vector<vector<int>>& grid) {
        return minPathSumIterative(grid);
    }
};
