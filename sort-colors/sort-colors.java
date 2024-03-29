class Solution {
    public void sortColors(int[] nums) {
        int lo=0, mid=0, hi=nums.length-1;
        while(mid <= hi) {
            if(nums[mid] == 0) {
                int temp = nums[lo];
                nums[lo] = nums[mid];
                nums[mid] = temp;
                lo++;
                mid = Math.max(lo, mid);
            }
            else if(nums[mid] == 1) {
                mid++;
            } else if(nums[mid] == 2) {
                int temp = nums[hi];
                nums[hi] = nums[mid];
                nums[mid] = temp;
                hi--;
            }
        }
    }
}