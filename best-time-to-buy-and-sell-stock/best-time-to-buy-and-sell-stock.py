class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        dp = [0, max(prices[1]-prices[0], 0)]
        minPrice = min(prices[0],prices[1])
        for i in range(2, len(prices)):
            dp += [ max(dp[i-1], prices[i] - minPrice) ]
            minPrice = min(minPrice, prices[i])
        return dp[-1]