class Solution {
public:
    vector<int> nums;
    unordered_map<int, bool> memo;
    vector<bool> dp;
    int totalSum;

    bool canPartition(vector<int>& nums) {
        this->nums = nums;
        totalSum = accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 != 0)
            return false;
        // return topDown(nums.size() - 1);
        dp = vector<bool>((totalSum / 2) + 1, false);
        return bottomUp();
    }

    bool bottomUp() {
        dp[0] = true;
        int leftSum = 0;
        for (int num : nums)
            for (int sum = dp.size() - 1; sum >= num; sum--)
                if (dp[sum - num])
                    dp[sum] = true;
        return dp.back();
    }

    bool topDown(int i, int leftSum = 0) {
        if (i < 0) {
            if (leftSum == totalSum / 2)
                return true;
            else
                return false;
        }
        int key = 20000 * i + leftSum;
        if (memo.count(key))
            return memo[key];
        if (topDown(i - 1, leftSum + nums[i]))
            return memo[key] = true;
        if (topDown(i - 1, leftSum))
            return memo[key] = true;
        return memo[key] = false;
    }
};