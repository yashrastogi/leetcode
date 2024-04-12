class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var counter = [Int: Int]()
        for num in nums {
            let temp = (counter[num] ?? 0) + 1
            counter[num] = temp
            if temp > nums.count / 2 { return num }
        }
        return 0
    }
}