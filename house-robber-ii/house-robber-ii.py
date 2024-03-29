class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        def dpdo(nums):
            l = len(nums)
            dp = [0 for _ in range(l)]
            dp[0], dp[1] = nums[0], max(nums[:2])
            for i in range(2, l):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        
        return max(dpdo(nums[1:]), dpdo(nums[:-1]))
        
        
        