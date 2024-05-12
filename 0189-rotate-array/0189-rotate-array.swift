class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var k = k
        while k != 0 {
            let temp = nums.popLast()!
            nums = [temp] + nums
            k -= 1
        }
    }
}