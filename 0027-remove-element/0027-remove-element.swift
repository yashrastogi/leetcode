class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var endI = nums.count - 1, i = 0
        
        while i <= endI {
            while endI > i && nums[endI] == val { endI -= 1 }
            if nums[i] == val {
                let temp = nums[endI]
                nums[endI] = nums[i]
                nums[i] = temp
                endI -= 1
            }
            i += 1
        }

        return endI + 1
    }
}