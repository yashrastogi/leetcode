class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int minSum = nums[0] + nums[1] + nums[2];
        for(int i=0; i<nums.length-2; i++) {
            int lo = i+1, hi = nums.length-1;
            while(lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                if (Math.abs(target-sum) < Math.abs(target-minSum)) {
                    minSum = sum;
                }
                if (sum == target) {
                    minSum = target;
                    break;
                } else if (sum < target) {
                    lo++;
                } else if (sum > target) {
                    hi--;
                }
            }
        }
        return minSum;
    }
}