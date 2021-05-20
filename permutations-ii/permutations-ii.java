class Solution {
    Set<List<Integer>> ret_set = new HashSet<List<Integer>>();
    int[] nums;
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        this.nums = nums;
        var map = new HashMap<Integer, Integer>();
        for(var num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        backtrack(new ArrayList<Integer>(), map);
        return new ArrayList<List<Integer>>(ret_set);
    }
    
    private void backtrack(List<Integer> curr, Map<Integer, Integer> map) {
        if(curr.size() == nums.length) {
            ret_set.add(new ArrayList<Integer>(curr));
        }
        for(int i=0; i<nums.length; i++) {
            if(map.get(nums[i]) > 0) {
                map.put(nums[i], map.get(nums[i])-1);
                curr.add(nums[i]);
                backtrack(curr, map);
                curr.remove(curr.size()-1);
                map.put(nums[i], map.get(nums[i])+1);
            }
        }
    }
}