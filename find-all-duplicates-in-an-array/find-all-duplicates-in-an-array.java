class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        var map = new HashMap<Integer, Integer>();
        var retArr = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        for(var a: map.entrySet()) {
            if(a.getValue() == 2) {
                retArr.add(a.getKey());
            }
        }
        return retArr;
    }
    
    public static void print(Object o) {
        System.out.println(o);
    }
}