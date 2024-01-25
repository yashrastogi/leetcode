class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0, j = 0;
        int curr_zeroes = 0;
        int max_ones = 0;

        while (j < nums.size()) {
            if (curr_zeroes > k) {
                if (nums[i] == 0) {
                    curr_zeroes -= 1;
                }
                i += 1;
            }

            if (nums[j] == 0) {
                curr_zeroes += 1;
            }

            int ones = j - i - curr_zeroes + 1;
            max_ones =
                max(max_ones, min(ones + k, static_cast<int>(nums.size())));
            j += 1;
        }

        return max_ones;
    }
};