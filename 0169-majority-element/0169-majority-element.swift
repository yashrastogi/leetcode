class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var lastNum = Int.max, lastNumCount = 0
        for num in nums {
            if lastNumCount == 0 {
                lastNum = num
                lastNumCount = 1
            } else  {
                lastNumCount += lastNum == num ? 1 : -1
            }
        }
        return lastNum
    }
}