class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int i = 0, j = 0, longestOneSubsequence = 0;
        bool usedPowerup = false;

        while (j < nums.size()) {
            if (nums[j] == 1) {
                if (usedPowerup) {
                    longestOneSubsequence = max(longestOneSubsequence, j - i);
                }
                if (!usedPowerup) {
                    longestOneSubsequence =
                        max(longestOneSubsequence, j - i + 1);
                }
                j += 1;
            } else if (!usedPowerup) {
                longestOneSubsequence = max(longestOneSubsequence, j - i);
                usedPowerup = true;
                j += 1;
            } else {
                while (nums[i++] != 0);
                usedPowerup = false;
            }
        }

        return min(longestOneSubsequence, int(nums.size()) - 1);
    }
};