class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        var intervals = intervals.sorted { $0[1] < $1[1] }
        var end = -50001
        var removeCount = 0
        for i in 0 ..< intervals.count {
            if intervals[i][0] < end {
                removeCount += 1
            } else {
                end = intervals[i][1]
            }
         }
        return removeCount
    }
}