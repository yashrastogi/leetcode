class Solution {
    func maxProfitIterative(_ prices: [Int], _ fee: Int) -> Int {
        // [i][0]: value when not holding any stock
        var dp00 = 0
        // [i][1]: value when holding a stock
        var dp01 = -prices[0]
        for i in 1 ..< prices.count {
            let oldDp00 = dp00
            dp00 = max(dp01 + prices[i] - fee, dp00)
            dp01 = max(oldDp00 - prices[i], dp01)
        }
        return max(dp00, dp01)
    }

    func maxProfitRecursive(_ prices: [Int], _ fee: Int) -> Int {
        var memo = [[Int]: Int]()

        func recursion(_ i: Int = 0, _ currValue: Int = 0, _ boughtStock: Bool = false) -> Int {
            if i == prices.count {
                return currValue
            }
            let key = [i, currValue, boughtStock ? 1 : 0]
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
        // return maxProfitRecursive(prices, fee)
        return maxProfitIterative(prices, fee)
    }
}
