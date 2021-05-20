class Solution {
    List<List<Integer>> ret = new ArrayList<List<Integer>>();
    int[] nums;
    
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        backtrack(new ArrayList<Integer>());
        return ret;
    }
    
    private void backtrack(List<Integer> curr) {
        if(curr.size() == nums.length) {
            ret.add(new ArrayList<Integer>(curr));
        }
        var set = new HashSet<Integer>(curr);
        for(int i=0; i<nums.length; i++) {
            if(!set.contains(nums[i])) {
                curr.add(nums[i]);
                backtrack(curr);
                curr.remove(curr.size()-1);
            }
        }
    }
}