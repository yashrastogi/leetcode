class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var counter = [Int: Int]()
        for num in nums {
            counter[num, default: 0] += 1
        }
        for (key, val) in counter {
            if val > nums.count / 2 {
                return key
            }
        }
        return 0
    }
}