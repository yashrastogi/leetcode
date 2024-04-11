class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var k = 0, lastNum = -101
        for i in 0 ..< nums.count { 
            if nums[i] != lastNum {
                lastNum = nums[i]
                let temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
            }
        }
        return k
    }
}