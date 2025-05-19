class Solution {
public:
    int findMin(vector<int> &nums) {
        int lo = 0, hi = nums.size() - 1, min_val = INT_MAX;
        while(lo <= hi) {
            int mid = lo + (hi-lo)/2;
            min_val = min(min_val, nums[mid]);
            if(nums[mid] > nums[hi]) {
                // right out of order
                lo = mid + 1;
            } else if (nums[mid] < nums[lo]) {
                // left out of order
                hi = mid - 1;
            }
            if (nums[mid] >= nums[lo]) { 
                // in order but need to go to left to find min
                min_val = min(nums[lo], min_val);
                hi = mid - 1;
            }
        }
        return min_val;
    }
};
