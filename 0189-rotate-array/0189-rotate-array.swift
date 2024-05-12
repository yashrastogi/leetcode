class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var k = k % nums.count
        let numReversed = Array(nums.reversed())
        nums = numReversed[0..<k].reversed() + nums[0..<(nums.count-k)]
    }
} 