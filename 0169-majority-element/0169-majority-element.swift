class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var counter = [Int: Int]()
        for num in nums {
            counter[num, default: 0] += 1
            if counter[num]! > nums.count / 2 {
                return num
            }
        }
        return 0
    }
}