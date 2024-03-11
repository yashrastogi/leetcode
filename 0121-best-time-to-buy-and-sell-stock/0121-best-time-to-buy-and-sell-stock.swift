class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minPrice = Int.max
        var maxProfit = 0
        for price in prices {
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        }
        return maxProfit
    }
}