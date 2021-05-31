#define vi vector<int>
#define vvi vector<vector<int>>

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int targetSum = accumulate(nums.begin(), nums.end(), 0);
        if (targetSum % 2 != 0) return false;
        targetSum /= 2;
        int l1 = nums.size() + 1, l2 = targetSum + 1; 
        vvi memo = vvi(l1, vi(l2, -1));
        return recursion(nums, nums.size(), targetSum, memo);
    }
    
    bool recursion(vi& nums, int idx, int rem, vvi& memo) {
        if(idx < 1) return false;
        if(rem < 0) return false;
        if(rem == 0) return true;
        if(int t = memo[idx][rem]; t != -1) return t;
        /*
            Choices:
            1. Take current idx, move to next idx
            2. Don't take current idx, move to next idx
        */
        return memo[idx][rem] = recursion(nums, idx - 1, rem - nums[idx - 1], memo) ||
               recursion(nums, idx - 1, rem, memo);
    }
};