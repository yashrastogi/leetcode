class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        var ret_set = new HashSet<List<Integer>>();
        
        for (int i=0; i<nums.length-2; i++) {
            if (i == 0 || nums[i-1] != nums[i]) {
                for(var pair: twoSum(i+1, nums.length-1, -nums[i], nums)) {
                    ret_set.add(Arrays.asList(new Integer[] {nums[i], pair[0], pair[1]}));
                }
            }
        }
        
        return new ArrayList<List<Integer>>(ret_set);
    }
    
    public List<int[]> twoSum(int lo, int hi, int target, int[] nums) {
        var ret = new ArrayList<int[]>();
        while (lo < hi) {
            int currSum = nums[lo] + nums[hi];
            if(currSum == target) {
                ret.add(new int[] {nums[lo], nums[hi]});
                hi--; 
                while(lo < hi && nums[lo] == nums[lo-1]){
                    lo++;
                }
            } else if(currSum < target) {
                lo++;
            } else if (currSum > target) {
                hi--;
            }
        }
        return ret;
    }
}