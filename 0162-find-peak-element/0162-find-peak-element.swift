class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        switch nums.count {
        case 1: return 0
        case 2: return nums[1] > nums[0] ? 1 : 2
        default: break
        }
        for i in 0 ..< nums.count {
            if i == 0 {
                if nums[i] > nums[i + 1] {
                    return i
                }
            } else if i == nums.count - 1 {
                if nums[i] > nums[i - 1] {
                    return i
                }
            } else if nums[i] > nums[i - 1] && nums[i] > nums[i + 1] {
                return i
            }
        }
        return -1
    }
}
