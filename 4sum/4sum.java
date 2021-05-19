class Solution {
    int[] nums;
    
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        this.nums = nums;
        return kSum(target, 0, 4);
    }
    
    public List<List<Integer>> kSum(int target, int lo, int k) {
        if(k == 2) {
            return twoSum(lo, target);
        }
        var ret = new ArrayList<List<Integer>>();
        
        for(int i=lo; i<nums.length-k+1; i++) {
            if(i == lo || nums[i] != nums[i-1]) {
                for(var pair: kSum(target-nums[i], i+1, k-1)) {
                    var temp = new ArrayList<Integer>();
                    temp.add(nums[i]);
                    for(var el: pair) {
                        temp.add(el);
                    }
                    ret.add(temp);
                }
            }
        }
        
        return ret;
    }
    
    public List<List<Integer>> twoSum(int lo, int target) {
        int start = lo, hi = nums.length-1;
        var ret = new ArrayList<List<Integer>>();
        while(lo < hi) {
            int sum = nums[lo] + nums[hi];
            if(sum == target) {
                ret.add(Arrays.asList(new Integer[] {nums[lo], nums[hi]}));
                hi--;
                do { lo++; } while(lo < hi && nums[lo] == nums[lo-1]);
            } else if(sum > target) {
                hi--;
            } else {
                lo++;
            }
        }
        return ret;
    }
} 