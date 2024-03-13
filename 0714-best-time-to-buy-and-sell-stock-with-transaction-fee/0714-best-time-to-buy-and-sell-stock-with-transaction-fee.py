class Solution:
    def maxProfitIterative(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2] * len(prices)
        maxValue = 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i] - fee, dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            maxValue = max(maxValue, dp[i][0], dp[i][1])
        return maxValue

    def maxProfitRecursive(self, prices: List[int], fee: int) -> int:
        memo = {}

        def recursion(i=0, currValue=0, boughtStock=False):
            if i == len(prices):
                return currValue
            key = (i, currValue, 1 if boughtStock else 0)
            if key in memo:
                return memo[key]
            result = 0
            if boughtStock:
                # Sell the stock and continue without holding
                sell_stock = recursion(i + 1, currValue + prices[i] - fee, False)
                # Continue without selling
                continue_holding = recursion(i + 1, currValue, True)
                result = max(sell_stock, continue_holding)
            else:
                # Buy the stock and continue holding
                buy_stock = recursion(i + 1, currValue - prices[i], True)
                # Continue without buying
                skip_buy = recursion(i + 1, currValue, False)
                result = max(buy_stock, skip_buy)
            memo[key] = result
            return result
        
        return recursion()

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.maxProfitIterative(prices, fee)
