class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[0], max(nums[:2])]
        dp += [0] * (len(nums)-2)
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]