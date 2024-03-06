class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var lo = 1
        var hi = piles.max()!
        while lo <= hi {
            let k = (hi - lo) / 2 + lo
            let kSum = piles.map { Int(ceil(Double($0) / Double(k))) }.reduce(0, +)
            if kSum <= h {
                hi = k - 1
            } else if kSum > h {
                lo = k + 1
            }
        }
        return lo
    }
}
