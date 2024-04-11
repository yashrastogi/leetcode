class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var k = 0, count = 0, lastNum = 10001
        for i in 0 ..< nums.count {
            if nums[i] != lastNum {
                lastNum = nums[i]
                count = 0
                let temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
            } else {
                count += 1
                if count >= 2 { continue }
                let temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
            }
        }
        return k
    }
}