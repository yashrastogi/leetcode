class Solution {
    public int findPeakElement(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while(lo < hi) {
            int mid = (hi - lo) / 2 + lo;
            if(nums[mid] < nums[mid + 1]) {
                lo += 1;
            } else {
                hi -= 1;
            }
        }
        return lo;
    }
}