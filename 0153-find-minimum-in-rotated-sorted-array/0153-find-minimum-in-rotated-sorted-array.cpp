class Solution {
  public:
    int findMin(vector<int> &nums) {
        return nums[getStartIndex(nums)];
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
        }
        else if (nums[mid] > nums[hi]) 
            return getStartIndex(nums, mid + 1, hi);
        else 
            return getStartIndex(nums, lo, mid - 1);
    }
};