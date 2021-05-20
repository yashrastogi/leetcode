class Solution {
    int[] candidates;
    List<List<Integer>> ret = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.candidates = candidates;
        backtrack(0, target, new ArrayList<Integer>(), 0);
        return this.ret;
    }
    
    public void backtrack(int idx, int target, List<Integer> curr, int sum) {
        if(idx == candidates.length) return;
        if(sum > target) return;
        if(sum == target) {
            ret.add(new ArrayList<Integer>(curr));
        }
        for(int i=idx; i<candidates.length; i++) {
            // choose
            curr.add(candidates[i]);
            backtrack(i, target, curr, sum+candidates[i]);
            curr.remove(curr.size()-1);
        }
        return;
    }
    
    
} 