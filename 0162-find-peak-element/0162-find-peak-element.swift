class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        var lo = 0
        var hi = nums.count - 1
        while lo < hi {
            let mid = (hi - lo) / 2 + lo
            if nums[mid] < nums[mid + 1] {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}