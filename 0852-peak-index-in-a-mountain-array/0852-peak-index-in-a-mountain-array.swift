class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var maxNum = -1, maxNumIndex = -1
        for (i, num) in arr.enumerated() {
            if num > maxNum {
                maxNum = num
                maxNumIndex = i
            }
        }
        return maxNumIndex
    }
}