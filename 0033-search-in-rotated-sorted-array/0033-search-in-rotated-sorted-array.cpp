class Solution {
  public:
    int search(vector<int> &nums, int target) {
        int start_index = getStartIndex(nums);
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int mid_index = (mid + start_index) % nums.size();
            if (nums[mid_index] < target) {
                lo = mid + 1;
            } else if (nums[mid_index] > target) {
                hi = mid - 1;
            } else {
                return mid_index;
            }
        }
        return -1;
    }

    int getStartIndex(vector<int> &nums, int lo = 0, int hi = INT_MAX) {
        if (hi == INT_MAX)
            hi = nums.size() - 1;
        if (lo > hi)
            return lo;
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] < nums[lo]) {
            int temp = getStartIndex(nums, lo, mid - 1);
            if (nums[mid] < nums[temp])
                return mid;
            else
                return temp;
        } else if (nums[mid] > nums[hi])
            return getStartIndex(nums, mid + 1, hi);
        else
            return getStartIndex(nums, lo, mid - 1);
    }
};
