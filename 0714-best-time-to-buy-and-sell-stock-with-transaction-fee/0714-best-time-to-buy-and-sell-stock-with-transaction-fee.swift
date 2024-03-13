class Solution {
    func maxProfitIterative(_ prices: [Int], _ fee: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: 2), count: prices.count)
        // [i][0]: value when not holding any stock
        dp[0][0] = 0
        // [i][1]: value when holding a stock
        dp[0][1] = -prices[0]
        for i in 1 ..< prices.count {
            dp[i][0] = max(dp[i - 1][1] + prices[i] - fee, dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        }
        return max(dp[prices.count - 1][0], dp[prices.count - 1][1])
    }

    var memo: [Int: Int] = [:]

    func maxProfitRecursive(_ prices: [Int], _ fee: Int) -> Int {
        func recursion(_ i: Int = 0, _ currValue: Int = 0, _ boughtStock: Bool = false) -> Int {
            if i == prices.count {
                return currValue
            }
            let key = (i << 1) | (boughtStock ? 1 : 0)
            if let memoized = memo[key] {
                return memoized
            }
            var result = 0
            if boughtStock {
                let sell_stock = recursion(i + 1, currValue + prices[i] - fee, false)
                let continue_holding = recursion(i + 1, currValue, true)
                result = max(sell_stock, continue_holding)
            } else {
                let buy_stock = recursion(i + 1, currValue - prices[i], true)
                let skip_buy = recursion(i + 1, currValue, false)
                result = max(buy_stock, skip_buy)
            }
            memo[key] = result
            return result
        }
        return recursion()
    }

    func maxProfit(_ prices: [Int], _ fee: Int) -> Int {
        return maxProfitIterative(prices, fee)
    }
}
