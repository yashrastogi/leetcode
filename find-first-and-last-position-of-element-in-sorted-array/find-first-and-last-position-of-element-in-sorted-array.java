class Solution {
    int[] nums;
    
    public int[] searchRange(int[] nums, int target) {
        this.nums = nums;
        int find = binarySearch(0, nums.length-1, target);
        if(find == -1) { return new int[] {-1, -1}; }
        int lb=find, ub=find;
        for(int i=lb-1; i>=0; i--) {
            if(nums[i] == nums[lb]) lb--;
        }
        for(int i=ub+1; i<nums.length; i++) {
            if(nums[i] == nums[ub]) ub++;
        }
        return new int[] {lb, ub};
    }
    
    public int binarySearch(int lo, int hi, int target) {
        if (lo < 0 || hi >= nums.length) return -1;
        
        int mid = (lo + hi) / 2;
        
        if (mid > hi || mid < lo) return -1;
        
        if(nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            return binarySearch(mid+1, hi, target);
        } else { // if (nums[mid] > target)
            return binarySearch(lo, mid-1, target);
        }
    }
}