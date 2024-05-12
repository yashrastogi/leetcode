class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var mprofit = 0, minprice = Int.max
        for p in prices {
            mprofit = max(mprofit, p - minprice)
            minprice = min(minprice, p)
        }    
        return mprofit
    }
}