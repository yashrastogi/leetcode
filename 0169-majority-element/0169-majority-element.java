public class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int lastNum = Integer.MAX_VALUE;
        int lastNumFreq = 0;
        for (int num : nums) {
            if (lastNum != num) {
                lastNum = num;
                lastNumFreq = 1;
            } else {
                lastNumFreq++;
            }
            if (lastNumFreq > nums.length / 2) {
                return lastNum;
            }
        }
        return 0;
    }
}
