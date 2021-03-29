class Solution {
    public static void print(Object o) {
        System.out.println(o);
    }
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++) {
            if(nums[i] != i)  {
                return i;
            }   
        }
        return nums.length;
    }
}