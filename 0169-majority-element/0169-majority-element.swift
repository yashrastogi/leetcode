class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var counter = [Int: Int]()
        for num in nums {
            counter[num, default: 0] += 1
        }
        var maxFreq = 0, maxFreqVal = -1
        for (key, val) in counter {
            if val > maxFreq {
                maxFreq = val
                maxFreqVal = key
            }
        }
        return maxFreqVal
    }
}