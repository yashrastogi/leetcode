class Solution {
    public int[] productExceptSelf(int[] nums) {
        var arrProduct = 1;
        var countZeroes = 0;
        for (var a: nums) {
            if (a != 0)
                arrProduct *= a;
            else {
                countZeroes++;
            }
        }
        var ans = new int[nums.length];
        Arrays.fill(ans, countZeroes > 0 ? 0 : arrProduct);
        for(int i=0; i<nums.length; i++) {
            if (nums[i] == 0 && countZeroes == 1) {
                ans[i] = arrProduct;
            } else if(nums[i] != 0) {
                ans[i] /= nums[i];    
            }
        }
        return ans;
    }
}