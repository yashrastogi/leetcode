class Solution {
    int[] candidates;
    // List<List<Integer>> ret = new ArrayList<List<Integer>>();
    Set<List<Integer>> ret_set = new HashSet<List<Integer>>();
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        this.candidates = candidates;
        recursion(0, new ArrayList<Integer>(), target);
        return new ArrayList<List<Integer>>(ret_set);
    }
    
    public void recursion(int idx, List<Integer> currList, int target) {
        if(idx == candidates.length) return;
        if(target < 0) return;
        if(candidates[idx] > target) return;
        var dup = new ArrayList<Integer>(currList);
        dup.add(candidates[idx]);
        if(candidates[idx] == target) {
        // System.out.println(dup + " " + target);
            ret_set.add(dup);
        }
        // case 1: keep on repeating current number, keep same idx
        recursion(idx, dup, target - candidates[idx]);
        // case 2: move to next number, increment idx, add current number to list
        recursion(idx+1, dup, target - candidates[idx]);
        // case 3: move to next number, increment idx, don't add current number to list
        recursion(idx+1, currList, target);
    }
}