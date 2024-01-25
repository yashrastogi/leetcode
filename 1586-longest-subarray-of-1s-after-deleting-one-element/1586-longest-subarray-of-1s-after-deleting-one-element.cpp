class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int i = 0, j = 0;
        int longestOneSubsequence = 0;
        bool usedPowerup = false;

        while (j < nums.size()) {
            if (nums[j] == 1) {
                if (usedPowerup) {
                    longestOneSubsequence = max(longestOneSubsequence, j - i);
                }
                if (!usedPowerup) {
                    longestOneSubsequence = max(longestOneSubsequence, j - i + 1);
                }
                j += 1;
            } else if (nums[j] == 0) {
                if (!usedPowerup) {
                    longestOneSubsequence = max(longestOneSubsequence, j - i);
                    usedPowerup = true;
                    j += 1;
                } else {
                    while (nums[i] != 0) {
                        i += 1;
                    }
                    i += 1;
                    usedPowerup = false;
                }
            }
        }

        if (longestOneSubsequence == nums.size()) {
            return nums.size() - 1;
        } else {
            return longestOneSubsequence;
        }
    }
};