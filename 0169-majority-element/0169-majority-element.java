public class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            int temp = counter.getOrDefault(num, 0) + 1;
            counter.put(num, temp);
            if (temp > nums.length / 2) {
                return num;
            }
        }
        return 0;
    }
}
