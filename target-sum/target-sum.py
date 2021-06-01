import pprint

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = 0
        for num in nums:
            totalSum += num
            
        if target > totalSum: return 0
        if (totalSum + target) % 2 != 0: return 0
        l1, l2 = len(nums) + 1, totalSum + 1
        dp = [[-1 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if i == 0: dp[i][j] = 0
                if j == 0: dp[i][j] = 1
        
        for i in range(1, l1):
            for j in range(0, l2):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        # pprint.pprint(dp)
        # s1+s2 = s ; s1-s2 = target ; s - 2s2 = target => (s - target)/2 = s2
        s2 = int((totalSum + target) / 2)
        # print(s2)
        return dp[len(nums)][s2]
        
        