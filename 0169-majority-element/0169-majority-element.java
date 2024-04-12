public class Solution {
    public int majorityElement(int[] nums) {
        int lastNum = Integer.MAX_VALUE;
        int lastNumCount = 0;
        
        for (int num : nums) {
            if (lastNumCount == 0) {
                lastNum = num;
                lastNumCount = 1;
            } else {
                lastNumCount += lastNum == num ? 1 : -1;
            }
        }
        
        return lastNum;
    }
}
