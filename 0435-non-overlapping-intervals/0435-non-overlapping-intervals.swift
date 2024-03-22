class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        var intervals = intervals.sorted { $0[1] > $1[1] }
        var end = -50001
        var removeCount = 0
        while let interval = intervals.popLast() {
            if interval[0] < end {
                removeCount += 1
            } else {
                end = interval[1]
            }
         }
        return removeCount
    }
}