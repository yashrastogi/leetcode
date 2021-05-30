class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum_nums = accumulate(nums.begin(), nums.end(), 0);
        if (sum_nums % 2 != 0) return false;
        int target_sum = sum_nums / 2;
        int l1 = nums.size() + 1, l2 = target_sum + 1;
        vector<vector<bool>> dp = vector<vector<bool>>(l1, vector<bool>(l2, 0));
        for(int i=0; i<l1; i++) {
            for(int j=0; j<l2; j++) {
                if(i == 0) 
                    dp[i][j] = 0;
                if(j == 0)
                    dp[i][j] = 1;
            }
        }
        
        for(int i=1; i<l1; i++) {
            for(int j=1; j<l2; j++) {
                /*
                    Choices (i is nums to consider, j is varing amount):
                    1. take current idx, move next idx
                    2. don't take current idx, move next idx --- default fallback
                */
                if(int t = j - nums[i-1]; t >= 0) {
                    dp[i][j] = dp[i-1][t] || dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
                
            }
        }
        return dp[nums.size()][target_sum];
    }
};