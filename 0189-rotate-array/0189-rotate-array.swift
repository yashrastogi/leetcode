class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var k = k % nums.count
        nums = Array(nums.reversed())[0..<k].reversed() + nums[0..<(nums.count-k)]
    }
} 