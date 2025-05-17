class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        int curr_max = -INT_MAX;
        int curr_max_last_idx = 0;
        for (int left = 0, right = 0; right < nums.size(); right++) {
            if (nums[right] >= curr_max) {
                curr_max = nums[right];
                curr_max_last_idx = right;
            }
            if (right - left + 1 < k)
                continue;
            else if (right - left + 1 > k) {
                left++;
                if (curr_max_last_idx < left) {
                    curr_max = -INT_MAX;
                    for (int temp = left; temp <= right; temp++) {
                        if (nums[temp] >= curr_max) {
                            curr_max = nums[temp];
                            curr_max_last_idx = temp;
                        }
                    }
                }
            }
            res.push_back(curr_max);
        }
        return res;
    }
};
