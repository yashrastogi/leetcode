class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # all LIS at least 1
        
        # LIS
        # LIS[-1] = 1
        # LIS[-2] = MAX(1, LIS[-1] + 1)
        # LIS[-3] = MAX(1, LIS[-2] + 1, LIS[-1] + 1)
        #                           |            |
        #      if nums[-2] > nums[-3] | if nums[-1] > nums[-3]
        # above logic can be condensed in below for loop
        max_dp = -float('inf')
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_dp = max(max_dp, dp[i])
        return max_dp