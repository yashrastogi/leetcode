class Solution {

    public int search(int[] nums, int target) {
        return partition(nums, target, 0, nums.length - 1);
    }

    public int partition(int[] nums, int target, int lo, int hi) {
        if(lo > hi) return -1;
        int mid = (hi + lo) / 2;
        if(target == nums[mid]) return mid;
        else if(target > nums[mid]) return partition(nums, target, mid + 1, hi);
        else return partition(nums, target, lo, mid - 1);
    }
}
