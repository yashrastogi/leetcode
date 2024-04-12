class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var nums = nums; nums.sort()
        var lastNum = Int.max, lastNumFreq = 0
        for num in nums {
            if lastNum != num {
                lastNum = num
                lastNumFreq = 1
            } else {
                lastNumFreq += 1
            }
            if lastNumFreq > nums.count / 2 {
                return lastNum
            }
        }
        return 0
    }
}