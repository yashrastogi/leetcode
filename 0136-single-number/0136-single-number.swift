class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var val = nums[0]
        for i in 1 ..< nums.count {
            val ^= nums[i]
        }
        return val
    }
}